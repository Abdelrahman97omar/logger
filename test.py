from pathlib import Path

credentials_folder=Path("~/.config/logger_credentials").expanduser()
credentials_folder.mkdir(parents=True, exist_ok=True)

credentials_file=credentials_folder / "credentials.txt"
# CLIENT_SECRET = input("Please enter the client secret: ")
# REFRESH_TOKEN = input("Please enter the refresh token: ")

# with open(credentials_file, "w") as f:
#     f.write(f"CLIENT_SECRET {CLIENT_SECRET} \n")
#     f.write(f"REFRESH_TOKEN {REFRESH_TOKEN} \n")



x = credentials_file.read_text().split("\n")
CLIENT_SECRET=x[0].split(" ")[1]
REFRESH_TOKEN=x[1].split(" ")[1]
print(CLIENT_SECRET)
print(REFRESH_TOKEN)
print(type(CLIENT_SECRET))
print(type(REFRESH_TOKEN))