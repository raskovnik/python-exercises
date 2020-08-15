from os import system
from time import sleep

while 1:
    try:
        system("eject cdrom")
        print("Ejecting...")
        sleep(5)
        system("eject -t cdrom")
        print("...")
        break
    except:
        print("error")