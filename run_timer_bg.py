#! /bin/python3

import subprocess
import sys

if len(sys.argv) <= 1:
    print("Provide minutes as well : <file> <minutes>")
    sys.exit(-1)
else:
    minutes = sys.argv[1]

with open("timer.log", "w", encoding="utf-8") as log_file:

    subprocess.Popen(
        [sys.executable, "-u", "-m", "src", str(minutes)],
        stdout=log_file,
        stderr=subprocess.STDOUT,
    )
