import os

if os.getuid == 0:
    print("not sudo")
    quit()

print("########################################")
print("########## INSTALLER STARTING ##########")
print("########################################")
print("")

# python3 packages
os.system("sudo apt install python3-tk")
os.system("sudo apt install python3-scapy")
os.system("sudo apt install python3-pyfiglet")
os.system("sudo apt install python3-bs4")
os.system("sudo apt install python3-dns")
os.system("sudo apt install python3-requests")
os.system("sudo apt install python3-phonenumbers")
os.system("sudo apt install python3-pyqt5")
os.system("sudo apt install python3-numpy")
os.system("sudo apt install python3-time")
os.system("sudo apt install python3-full")

# basic packages
os.system("sudo apt install neofetch")
os.system("sudo apt install nano")
os.system("sudo apt install mono-complete")
os.system("sudo apt install python3")
os.system("neofetch")

print("########################################")
print("########## INSTALLER COMPLETE ##########")
print("########################################")
os.system("sudo python3 run.py")
