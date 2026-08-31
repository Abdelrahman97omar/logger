# Install logger:
Run the following in the same order:</br> 
1. If you are installing the logger for the first time, run: **pip install --upgrade pip** 
2. pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/Abdelrahman97omar/logger.git
3. Run the folloeing command by copy.paste in terminal: ~/.local/bin/logger-install
4. The logger.py, creatreport.py and install_service.py (package installer) will be installed into /home/.local/lib/python3.10/site-packages/logger_system  
5. The logs file (logs.txt) and the report pdf (latest-stats.pdf) will be in /home/.logs
6. In in line 7 in logger.py file, choose which country will the robot be operating in order to choose the time zone

# Send periodic mail with the reports:
1. Go to https://api-console.zoho.com/, choose self client, then in **Generate Code**, enter `ZohoMail.messages.ALL,ZohoMail.accounts.READ` in scope section and generate temporary Auth key. Then generate Client ID and Client Secret from **client secret**.
2. Use the generated code to in `getAccessToken.py` script to get the access token.
3. Use the access token to generate the account_id from `getAccountId.py`
4. Now we have account_id and access_token, so we can use them anywhere we want to communicate with the mail api.
5. Before sending the mail with the attachment, we need to upload the files (attachments) to zoho server using `uploadFiles`.
6. Use `sendMail.py` in order to send the mail.
