import os

if os.getuid == 0:
    print("not sudo")


print("########################################")
print("########## INSTALLER STARTING ##########")
print("########################################")
print("")

os.system("sudo apt install neofetch")
os.system("sudo apt install nano")
os.system("sudo apt install mono-complete")
os.system("sudo apt install python3")
os.system("neofetch")

print("########################################")
print("########## INSTALLER COMPLETE ##########")
print("########################################")
os.system("sudo python3 run.py")
