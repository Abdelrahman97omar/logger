
import requests
import os
from  pathlib import Path

url = "https://mail.zoho.com/api/accounts/8804211000000008002/messages"

user=os.getenv("USER","Unknow")
robot_id=os.getenv("ROBOT_ID","UNKNOWN")


credentials_folder=Path("~/.config/logger_credentials").expanduser()
credentials_file=credentials_folder / "credentials.txt"
file_content = credentials_file.read_text().split("\n")
CLIENT_SECRET=file_content[0].split(" ")[1]
REFRESH_TOKEN=file_content[1].split(" ")[1]

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Zoho-oauthtoken 1000.d81e614c0fe4a0a1f0813163e68c63af.383e7578bcfca987222f1d82ed8d52ff",
}

data = {
    "fromAddress": "abdelrahman.omar@marses.systems",
    "toAddress": "hadeer.ahmed@marses.systems",
    # "ccAddress": "colleagues@mywork.com",
    # "bccAddress": "restadmin1@restapi.com",
    "subject": "test",
    "content": f"The monthly report for {user}_{robot_id} is ready. Please find the report attached.",
"attachments": [
    {
        "storeName": "856804851",
        "attachmentPath": "/Mail/7d623991659f49d992a8c-latest-stats.pdf",
        "attachmentName": "latest-stats.pdf",
    }
],
}

response = requests.post(
    url,
    headers=headers,
    json=data,
)

print(response.status_code)
print(response.text)



