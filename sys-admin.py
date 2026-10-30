import os
import subprocess

print("=== Exercise 1: os.system ===")
os.system("ls")

print("=== Exercise 2: subprocess.run ===")
subprocess.run(["ls"])

print("=== Exercise 3: subprocess.run with two arguments ===")
subprocess.run(["ls", "-l"])

print("=== Exercise 4: subprocess.run with three arguments ===")
subprocess.run(["ls", "-l", "README.md"])

print("=== Exercise 5: system information ===")
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

print("=== Exercise 6: active processes ===")
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

print("=== Bonus: disk space ===")
subprocess.run(["df", "-h"])
