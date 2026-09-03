import os
import requests
import shutil
from pathlib import Path
from datetime import datetime



USER=os.getenv("USER","Unknow")
ROBOT_ID=os.getenv("ROBOT_ID","UNKNOWN")
credentials_folder=Path("~/.config/logger_credentials").expanduser()
credentials_file=credentials_folder / "credentials.txt"
ROBOT_HOME = Path.home()
LOGS_DIR = ROBOT_HOME / ".logs"
PDF_PATH = LOGS_DIR / "latest-stats.pdf"
STATE_FILE = LOGS_DIR / "last_sent.txt"


CLIENT_ID = "1000.GE627XEHE9ME97OVER7S1YOIC1CRUE"
ACCOUNT_ID = "8804211000000008002"
FROM_ADDRESS = "abdelrahman.omar@marses.systems"
TO_ADDRESS =   "abdalrahman.hazem@marses.systems"
#================= Sectrets ======================
file_content = credentials_file.read_text().split("\n")
CLIENT_SECRET=file_content[0].split(" ")[1]
REFRESH_TOKEN=file_content[1].split(" ")[1]
#=================================================


if not STATE_FILE.exists():
    STATE_FILE.write_text("")

# ============================================================
# 0. Check the state of the file for this month
# ============================================================
if not STATE_FILE.exists():
    STATE_FILE.write_text("")

def get_last_sent_month():
    if not STATE_FILE.exists():
        return None
    return STATE_FILE.read_text().strip()

def mark_month_as_sent():
    current_month = datetime.now().strftime("%Y-%m")
    STATE_FILE.write_text(current_month)

def already_sent_this_month():
    current_month = datetime.now().strftime("%Y-%m")
    last_sent_month = get_last_sent_month()
    return last_sent_month == current_month

# ============================================================
# 1. Get a fresh access token
# ============================================================

def get_access_token():

    response = requests.post(
        "https://accounts.zoho.com/oauth/v2/token",
        params={
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "refresh_token",
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    return data["access_token"]


# ============================================================
# 2. Upload PDF to Zoho
# ============================================================

def upload_attachment(access_token):

    url = (
        f"https://mail.zoho.com/api/accounts/"
        f"{ACCOUNT_ID}/messages/attachments"
    )

    headers = {
        "Accept": "application/json",
        "Authorization": f"Zoho-oauthtoken {access_token}",
    }

    params = {
        "uploadType": "multipart",
        "isInline": "false",
    }

    with open(PDF_PATH, "rb") as f:

        files = {
            "attach": (
                os.path.basename(PDF_PATH),
                f,
                "application/pdf",
            )
        }

        response = requests.post(
            url,
            headers=headers,
            params=params,
            files=files,
            timeout=60,
        )

    response.raise_for_status()

    data = response.json()["data"][0]

    return {
        "storeName": data["storeName"],
        "attachmentPath": data["attachmentPath"],
        "attachmentName": data["attachmentName"],
    }


# ============================================================
# 3. Send email
# ============================================================

def send_email(access_token, attachment):

    url = (
        f"https://mail.zoho.com/api/accounts/"
        f"{ACCOUNT_ID}/messages"
    )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Zoho-oauthtoken {access_token}",
    }

    data = {
        "fromAddress": FROM_ADDRESS,
        "toAddress": TO_ADDRESS,

        "subject": "Monthly Report",

        "content": (
            "Hello,\n\n"
            f"The monthly report for {USER}_{ROBOT_ID} is ready. Please find the report attached."
            "Regards"
        ),

        "attachments": [
            attachment
        ],
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=60,
    )

    response.raise_for_status()
    result = response.json()

    #move succfully sent file to "old_logs folder"
    if result.get("status", {}).get("code") == 200:
        old_logs_dir = LOGS_DIR / "old_logs"
        old_logs_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    shutil.move(LOGS_DIR / "logs.txt",old_logs_dir / f"logs_{timestamp}.txt")
    shutil.move(LOGS_DIR / "latest-stats.pdf",old_logs_dir / f"latest-stats_{timestamp}.pdf")
    return response.json()


# ============================================================
# Main
# ============================================================

def main():
    if already_sent_this_month():
        print("Already sent this month.")
        return
    try:
        access_token = get_access_token()
        attachment = upload_attachment(access_token)
        send_email(access_token, attachment)
        mark_month_as_sent()
        print("SUCCESS: Monthly report sent.")
    except Exception as e:
        print(f"FAILED: {e}")
        print("Will retry on the next scheduled run.")

if __name__ == "__main__":
    main()