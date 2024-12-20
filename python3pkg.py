import os

if os.getuid == 0:
    print("not sudo")
    quit()






print("########################################")
print("########## INSTALLER STARTING ##########")
print("########################################")
print("")

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


print("########################################")
print("########## INSTALLER COMPLETE ##########")
print("########################################")
os.system("sudo python3 run.py")






