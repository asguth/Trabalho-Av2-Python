import time
import os

def clear():
    os.system("cls")

clear()
print ("\nCálculo da área do trapézio")
time.sleep(2)
clear()

bma = float(input("\nDigite a base MAIOR do trapézio: "))
clear()

bmm = float(input("\nDigite a base MENOR do trapézio: "))
clear()

alt = float(input("\nDigite a ALTURA do trapézio: "))
clear()

area = (( bma + bmm ) * alt ) / 2

print (f"\nA Área do Trapézio é :{area}")
time.sleep(10)