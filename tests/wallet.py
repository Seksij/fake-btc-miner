import string,random
import colorama
import time
from colored import fg

from colorama import init, Fore
init(convert = True)


LicenseKey = input("input license key:   ")

print(Fore.RED + "Checking if key is valid.....   ")

time.sleep(3)
print("Key is Valid")

Wallet = input("Wallet: ")

print("Checking if wallet exists....  ")
time.sleep(4)
print("Wallet Found!")
time.sleep(2)
print("Set up workspace for you....  ")
time.sleep(4)



for x in range(2, 400000):
    print("".join(random.choice(string.ascii_letters + string.digits)for i in range(63)) + " [x]Trying again. -> 0.0000 BTC")


print (Fore.GREEN + '0xC257274276a4E539741Ca11b590B9447B26A8051 -> 1.234 BTC')


print("Cracked")
print(Fore.BLUE + "Transfering all BTC to wallet.... ")
time.sleep(10)
print(Fore.BLUE + "BTC has been transferd! ")
str(input("Press any key to mine again"))
str(input("to mine again just re-open the miner"))

red = fg('red')
print (red)