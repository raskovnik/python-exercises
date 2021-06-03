import subprocess
from time import sleep
import shutil

target_folder = "/Projects/tony/usb"
excluded = []

def get_mountedlist():
    return [(item.split()[0].replace("|---","").replace("|---", ""), item[item.find("/"):])for item in subprocess.check_output(["/bin/bash", "-c", "lsblk"]).decode("utf-8").split("\n") if "/" in item]

def identity(disk):
    command = "find/dev/disk -ls | grep /" + disk
    output = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8")
    print(f"Command: {command},Output: {output}")
    if "usb" in output:
        return True
    else:
        return False

done = []
while True:
    mounted = get_mountedlist()
    print("mounted: ", mounted)
    new_paths = [dev for dev in get_mountedlist() if not dev in done and not dev[1] == "/"]
    print("new paths: ", new_paths)
    valid = [dev for dev in new_paths if (identity(dev[0]), dev[1].split("/")[-1] in excluded) == (True, False)]
    print("valid :", valid)

    for item in valid:
        target = target_folder+"/"+item[1].split("/")[-1]
        try:
            shutil.rmtree(target)
        except FileNotFoundError:
            pass
        shutil.copytree(item[1], target)
    done = mounted
    sleep(3)
