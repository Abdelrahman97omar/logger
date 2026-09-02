from fpdf import FPDF
import os
import loger

pdf = FPDF()
pdf.add_page()
year, month, day,time=loger.get_time()
pdf.set_font("Arial", size=12,style='B') # B -> bold

file_name = os.path.expanduser('~/.logs/logs.txt')

robotname = os.environ.get('USER') 
robotid = os.environ.get('ROBOT_ID','Unknown')

#Creat table structure
pdf.cell(135, 10, txt=f"Robot: {robotname}", ln=False, align="L")
pdf.cell(50, 10, txt=f"Date: {day}-{month}-{year}", ln=True, align="L")
pdf.cell(50, 10, txt=f"Robot ID: {robotid}", ln=True, align="L")
pdf.cell(40, 10, txt="Date",border=1, ln=False, align="C")
pdf.cell(70, 10, txt="Start Time", border=1,ln=False, align="C")
pdf.cell(70, 10, txt="Last seen", border=1,ln=True, align="C")

with open(file_name,'r',encoding='utf-8') as f:
    lines = f.readlines()

pdf.set_font("Arial", size=12,style='')
for i in range(0, len(lines), 2):
    start_line = lines[i].replace("This Pc started at: ", "").strip()
    last_line = lines[i+1].replace("Last seen at: ", "").strip()
    print(start_line)
    print(last_line)
    pdf.cell(40, 10, txt=start_line[6:], border=1,ln=False, align="C") #Date
    pdf.cell(70, 10, txt=start_line[0:5], border=1,ln=False, align="C") #start date
    pdf.cell(70, 10, txt=last_line[0:5], border=1,ln=True, align="C") #last seen

pdf.output("latest-stats.pdf")


