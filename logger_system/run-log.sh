#!/bin/bash
PYTHON=$(command -v python3)
LOGGER_DIR=$("$PYTHON" -c 'import logger_system, os; print(os.path.dirname(logger_system.__file__))')

"$PYTHON" "${LOGGER_DIR}/creatreport.py"
sleep 30
"$PYTHON" "${LOGGER_DIR}/loger.py"

