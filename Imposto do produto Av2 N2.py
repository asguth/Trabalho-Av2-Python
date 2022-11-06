import time
import os

def clean():
    os.system("cls")

def soma_imposto(taxa_imposto, Custo):
    return (1 + taxa_imposto/100)*Custo

clean()
print("\nCalculo Imposto sobre o produto")
time.sleep(2)

clean()
tax = float(input("\nDigite a TAXA em porcentagem de imposto: "))
cus = float(input("\nDigite o CUSTO do produto: "))

print(f"\nValor do produto com imposto: {soma_imposto(tax,cus):.2f}")
time.sleep(10)