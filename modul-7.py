#1
#finns i tidigare uppgifter jag gjort(listan och gissa nummret)

#2

import time 
tal = input("skriv ett tal du vill addera:")
tal1= input("skriv ett tal du vill addera:")
print("Beräknar svar")
for x in range(0,3):
    time.sleep(1)
    print(".")
time.sleep(1)
print(int(tal)+int(tal1))

#3

import msvcrt

print("välkomen ...\ntryck på q för att avsluta.")
test = msvcrt.getwch()
if test == "q":
    print("hejdå")
elif test != "":
    print("det var inte q")


#4
from colors import bcolors
print(bcolors.BLUE+"deta är färgat"+bcolors.WHITE)

#5
print(bcolors.BLUE+"R"+bcolors.CYAN+"a"+bcolors.GREEN+"i"+bcolors.YELLOW+"n"+bcolors.PURPLE+"b"+bcolors.RED+"o"+bcolors.GREEN+"w")

#6
print("skriv a eller b")
p = msvcrt.getwch()
if p == "a":
    print("a")
elif p == "b":
    print("b")

