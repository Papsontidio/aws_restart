import os
import subprocess

name = "README.md; echo HACKED"
print("--- os.system (command built from a string) ---")
os.system("ls -l " + name)
print("--- subprocess.run (arguments as a list) ---")
subprocess.run(["ls", "-l", name])
