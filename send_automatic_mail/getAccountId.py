import requests

access_token = "1000.9e16dfd9d36fe665c6b7c814c9eea647.2386389772e166169c45adce06bdac62"
response = requests.get(
    "https://mail.zoho.com/api/accounts",
    headers={
        "Authorization": f"Zoho-oauthtoken {access_token}"
    },
)

print(response.status_code)
print(response.json())