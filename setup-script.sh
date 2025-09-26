#! /bin/bash

python -m venv .venv
source .venv/bin/activate
echo "Virtual environment activated"

pip install --upgrade pip
pip install -r requirements.txt

cp run_timer_bg.py timer
chmod +x timer

cp timer_logs.sh timer_logs

chmod +x timer_logs


PROJECT_DIR=$(pwd)
echo "export PATH=\"$PROJECT_DIR:\$PATH\"" >> ~/.bashrc
source ~/.bashrc
echo "Successfully setup the timer"








