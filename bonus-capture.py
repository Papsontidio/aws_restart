import subprocess

result = subprocess.run(["uname", "-s"], capture_output=True, text=True)
print("Output:", result.stdout.strip())
print("Return code:", result.returncode)

bad = subprocess.run(["ls", "/does-not-exist"], capture_output=True, text=True)
print("Return code:", bad.returncode)
print("Error:", bad.stderr.strip())
