# Logger Installation

Follow the steps below in the specified order.

## Standard Installation

1. **Upgrade pip**

   If this is the first time installing the logger, upgrade `pip`:

   ```bash
   pip install --upgrade pip
   ```

2. **Install the logger package**

   ```bash
   pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/Abdelrahman97omar/logger.git
   ```

3. **Run the installation script**

   Copy and paste the following command into the terminal:

   ```bash
   ~/.local/bin/logger-install
   ```

4. **Installed files**

   The following files will be installed under:

   ```text
   /home/<user>/.local/lib/python3.<version>/site-packages/logger_system/
   ```

   The package includes:

   * `logger.py`
   * `creatreport.py`
   * `install_service.py`
   * `run-log.sh`

5. **Log and report files**

   The logger will store the generated files under:

   ```text
   /home/<user>/.logs/
   ```

   This directory contains:

   * `logs.txt` — the logger output file.
   * `latest-stats.pdf` — the latest generated report.
   * `last_sent.txt` — record of the date where last report was sent.
   * `old_logs` — folder containg all old logs files. Those files where sent in previous months
   * `mail-cron.log` — logs for the automatic mail sending system.
       


6. **Configure the robot's time zone**

   Open `logger.py` and update the country configuration on **line 7**.

   Select the country where the robot will be operating to ensure that the correct time zone is used.

---

# Installation on Older Ubuntu Versions

The logger requires **Python 3.7 or later**.

If you are installing the logger on an older Ubuntu system, follow these steps.

## 1. Check the installed Python versions

Check the available Python versions installed on the system:

```bash
ls /usr/bin/python3*
```

Alternatively:

```bash
ls /usr/local/bin/python3*
```

Identify the **latest Python 3 version** available on the system.

If Python 3.7 or later is already installed, use that version for the remaining steps.

## 2. Install Python 3.7 or later if required

If no Python version **3.7 or later** is available, install a compatible Python version before proceeding.

## 3. Upgrade pip

Use the Python version you identified above:

```bash
python3.<version> -m pip install --upgrade pip
```

For example:

```bash
python3.7 -m pip install --upgrade pip
```

## 4. Install the logger package

Install the package using the same Python version:

```bash
python3.<version> -m pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/Abdelrahman97omar/logger.git
```

For example, with Python 3.7:

```bash
python3.7 -m pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/Abdelrahman97omar/logger.git
```

> **Important:** Replace `<version>` with the Python version used to install the `logger_system` package. Use the **same Python version throughout the installation**.

## 5. Run the installation script

Copy and paste the following command into the terminal:

```bash
~/.local/bin/logger-install
```

## 6. Update `run-log.sh`

Locate the following file:

```text
/home/<user>/.local/lib/python3.<version>/site-packages/logger_system/run-log.sh
```

Open the file and locate:

```bash
PYTHON=$(command -v python3)
```

Replace it with:

```bash
PYTHON=$(command -v python3.<version>)
```

For example, if the logger was installed using Python 3.7:

```bash
PYTHON=$(command -v python3.7)
```

> **Important:** `<version>` must match the Python version used to install `logger_system`.

## 7. Update the systemd service

Open the logger systemd service:

```text
/etc/systemd/system/logger.service
```

Locate the following line:

```ini
ExecStart=/bin/bash -c '"$(python3 -m site --user-site)/logger_system/run-log.sh"'
```

Replace it with:

```ini
ExecStart=/bin/bash -c '"$(python3.<version> -m site --user-site)/logger_system/run-log.sh"'
```

For example, when using Python 3.7:

```ini
ExecStart=/bin/bash -c '"$(python3.7 -m site --user-site)/logger_system/run-log.sh"'
```

> **Important:** The Python version specified here must match the Python version used to install `logger_system`. This ensures that both the systemd service and `run-log.sh` use the correct Python installation.

After modifying the systemd service, reload the systemd configuration:

```bash
sudo systemctl daemon-reload
```

Then restart the logger service:

```bash
sudo systemctl restart logger.service
```

Verify the service status:

```bash
sudo systemctl status logger.service
```

---

# Testing Periodic Email Reports

The following steps describe how to test sending periodic reports by email using the Zoho Mail API.

## 1. Create Zoho API credentials

Go to the [Zoho API Console](https://api-console.zoho.com/) and create a **Self Client**.

Under **Generate Code**, use the following scopes:

```text
ZohoMail.messages.ALL,ZohoMail.accounts.READ
```

Generate a temporary authorization code.

Then generate the required **Client ID** and **Client Secret** from the client configuration.

## 2. Generate an access token

Use the generated authorization code with `getAccessToken.py` to obtain an access token.

## 3. Retrieve the account ID

Use the access token with `getAccountId.py` to retrieve the Zoho Mail `account_id`.

At this point, you should have:

* `client_id`
* `client_secret`
* `access_token`
* `account_id`

These credentials can be used to communicate with the Zoho Mail API.

## 4. Upload email attachments

Before sending an email with attachments, upload the required files to the Zoho server using `uploadFiles`.

## 5. Send the email

Use `sendMail.py` to send the email and include the uploaded files as attachments.

---

## Summary

The logger requires **Python 3.7 or later**. On systems with multiple Python installations, always use the same Python version to:

1. Upgrade `pip`.
2. Install the `logger_system` package.
3. Configure `run-log.sh`.
4. Configure the systemd service.

This ensures that the logger consistently uses the Python environment where the package is installed.
