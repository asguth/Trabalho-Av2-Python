import time
import os
import sys

def clean():
    os.system("cls")

clean()
print("\nConversor Hora AM/PM")
time.sleep(2)
clean()

hr = int(input("\nDigite a(s) hora(s): "))
min = int(input("Digite o(s) minuto(s): "))
A = ("AM")
P = ("PM")

def conversao(hr):
    return (hr - 12)

def saida(hr,min):
    if(hr > 24 or min > 59):
        print("\nPrograma finalizado com a exceção SystemExit em (10 Segundos), (ERRO: Hr > 24 ou Min > 59)")
        time.sleep(10)
        sys.exit()
    
    print("\nHorário Convertido: ")
    
    if(min < 10):
        min = (f"0{min}")
    
    if(hr == 0):
        hr += 12
    
    if(hr <= 12):
        print(hr,":",min, A)
    
    else:
        print(conversao(hr),":", min, P)

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