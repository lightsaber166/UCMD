import os

with open("autorun.txt", "r") as f:
    os.system(f.read())
with open("prompt.txt", "r") as f:
    prompt = f.read()
while True:
    cmd = input(prompt + " ")
    os.system(cmd)