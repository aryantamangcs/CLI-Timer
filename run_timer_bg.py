import subprocess
import sys

if len(sys.argv) <= 1:
    print("Provide minutes as well : <file> <minutes>")
    sys.exit(-1)
else:
    minutes = sys.argv[1]

subprocess.Popen(
    [sys.executable, "-u", "-m", "src", str(minutes)],
    stdout=open("timer.log", "w"),
    stderr=subprocess.STDOUT,
)
