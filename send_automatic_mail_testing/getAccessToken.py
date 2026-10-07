import requests

response = requests.post(
    "https://accounts.zoho.com/oauth/v2/token",
    params={
        "code": "1000.3bef023c8c74361efb05b12b358f1ada.984c72e25f665816e17b7d9242926c27",
        "grant_type": "authorization_code",
        "client_id": "1000.GE627XEHE9ME97OVER7S1YOIC1CRUE",
        "client_secret": "e46b30965f29b765445e9ba99262ee1446f6fe5453",
    },
)

print(response.status_code)
print(response.json())
