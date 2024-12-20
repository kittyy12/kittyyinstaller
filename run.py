import os
import time


print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("##########################")
time.sleep(0.05)
print(" ######################## ")
time.sleep(0.05)
print("  ######################  ")
time.sleep(0.05)
print("   ####################   ")
time.sleep(0.05)
print("    ##################    ")
time.sleep(0.05)
print("     ################     ")
time.sleep(0.05)
print("      ##############      ")
time.sleep(0.05)
print("       ############       ")
time.sleep(0.05)
print("        ##########        ")
time.sleep(0.05)
print("         ########         ")
time.sleep(0.05)
print("          ######          ")
time.sleep(0.05)
print("           ####           ")
time.sleep(0.05)
print("            ##            ")
print("")
print("-----KittyyInstaller-----")
print("")
print("made by Kittyy :3")
print("")
print("")
print("-----------------------------------------------------------------")
print("[1] python3 packages   |   [2] basic packages like neofetch")
print("[3] all (of this installer)   |   [4] what is being installed?")
print("[5] quit")
print("-----------------------------------------------------------------")


packagesbi = """
###### python3 packges ######

tkinter
scapy
pyfiglet
bs4
dns
requests
phonenumbers
pyqt5
numpy
time
python3-full
------------------------------
###### basic packages ######

neofetch
nano
mono-complete
python3
-runs neofetch at the end-
------------------------------
###### all packages ######

tkinter
scapy
pyfiglet
bs4
dns
requests
phonenumbers
pyqt5
numpy
time
python3-full
neofetch
nano
mono-complete
python3
-runs neofetch at the end-

"""


userinput = input("==> ")
if userinput == '1':
    print("starting installer..")
    os.system("sudo python3 python3pkg.py")
        
if userinput == '2':
    print("starting script..")
    os.system("sudo python3 basicpkg.py")

elif userinput == '4':
    print(packagesbi)

if userinput == '3':
    print("starting script..")
    os.system("sudo python3 allpkg.py")

