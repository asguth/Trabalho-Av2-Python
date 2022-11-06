import time
import os

def clean():
    os.system("cls")

clean()
print("\nConversor Hora AM/PM")
time.sleep(2)
clean()

hr = int(input("\nDigite a(s) hora(s): "))
min = int(input("Digite o(s) minuto(s): "))

def conversao(hr):
    return (hr - 12)

def saida(hr,min):
    
    print("\nHorário Convertido: ")
    
    if(min < 10):
        min = (f"0{min}")
    
    if(hr <= 12):
        print(hr,":",min,"AM")
    else:
        print(conversao(hr),":", min, "PM")

saida(hr, min)
time.sleep(5)

while True:
   clean()
   hr = int(input("\nDigite um valor negativo para sair | ou | Digite a(s) hora(s): "))
   if hr < 0:
    break

   min = int(input("Digite o(s) minuto(s): "))
   saida(hr,min)
   time.sleep(5)