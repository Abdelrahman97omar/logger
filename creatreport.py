from fpdf import FPDF
import os
import loger

pdf = FPDF()
pdf.add_page()
year, month, day,time=loger.get_time()
pdf.set_font("Arial", size=12,style='B') # B -> bold

robotname = os.environ.get('USER') 
robotid = os.environ.get('ROBOT_ID')

#Creat table structure
pdf.cell(135, 10, txt=f"Robot: {robotname}", ln=False, align="L",)
pdf.cell(50, 10, txt=f"Date: {day}-{month}-{year}", ln=True, align="L")
pdf.cell(50, 10, txt=f"Robot ID: {robotid}", ln=True, align="L")
pdf.cell(40, 10, txt="Date",border=1, ln=False, align="C")
pdf.cell(70, 10, txt="Start Time", border=1,ln=False, align="C")
pdf.cell(70, 10, txt="Last seen", border=1,ln=True, align="C")

with open('logs.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

pdf.set_font("Arial", size=12,style='')
for i in range(0, len(lines), 2):
    start_line = lines[i].strip("This Pc started at: ")
    start_line = start_line.strip()
    last_line = lines[i+1].strip("Last seen at: ")
    last_line = last_line.strip()

    pdf.cell(40, 10, txt=start_line[6:], border=1,ln=False, align="C") #Date
    pdf.cell(70, 10, txt=start_line[0:5], border=1,ln=False, align="C") #start date
    pdf.cell(70, 10, txt=last_line[0:5], border=1,ln=True, align="C") #last seen

pdf.output("latest-stats.pdf")
