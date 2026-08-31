import requests

account_id = "8804211000000008002"
access_token = "1000.9e16dfd9d36fe665c6b7c814c9eea647.2386389772e166169c45adce06bdac62"

url = f"https://mail.zoho.com/api/accounts/{account_id}/messages/attachments"

params = {
    "uploadType": "multipart",
    "isInline": "false"
}

headers = {
    "Accept": "application/json",
    "Authorization": f"Zoho-oauthtoken {access_token}"
}

with open("/home/abdelrahman/.logs/latest-stats.pdf", "rb") as f:
    files = {
        "attach": (
            "latest-stats.pdf",
            f,
            "application/pdf"
        )
    }

    response = requests.post(
        url,
        headers=headers,
        params=params,
        files=files
    )

print(response.status_code)
print(response.text)

