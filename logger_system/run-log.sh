#!/bin/bash
SITE_PACKAGES=$(ls -d /home/${USER}/.local/lib/python3.*/site-packages 2>/dev/null | head -n 1)
python3 "${SITE_PACKAGES}/logger_system/creatreport.py"
sleep 30
python3 "${SITE_PACKAGES}/logger_system/loger.py"