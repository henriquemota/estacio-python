# 2. Escreva um script python para ler todas as
# linhas de um arquivo, ordena-las e salvar novamente no arquivo.
import random
import os
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

with open(path.join(BASE_DIR, "data.txt"), "w") as file:
    for i in range(100):
        num = random.randint(1, 1000)
        file.write(f"{num}\n")

with open(path.join(BASE_DIR, "data.txt")) as file:
    linhas = file.readlines()
    numeros = []
    for linha in linhas:
        numeros.append(int(linha))

    numeros.sort()
    with open(path.join(BASE_DIR, "ordenados.txt"), "w") as file:
        for numero in numeros:
            file.write(f"{numero}\n")
            print(numero)
