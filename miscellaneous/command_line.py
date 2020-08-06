import os, os.path, sys, readline

def modcmd(arg):
    os.system(sys.executable+" "+sys.prefix+"/bin/sh/"+arg)

if not os.path.exists(sys.prefix+"/bin/sh"):
    print("Directory isn't found.")

while True:
    cmd = input("==>")
    if cmd == "":
        break
    modcmd(cmd)