
import requests

url = "https://mail.zoho.com/api/accounts/8804211000000008002/messages"

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
    "content": "Email can never be dead. The most neutral and effective way, that can be used for one to many and two way communication.",
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



