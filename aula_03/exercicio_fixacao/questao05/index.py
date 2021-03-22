# 5. Faça um programa que leia um número N e gere um
# arquivo com N nomes e idades aleatórios.
# Faça uso de duas listas criadas na mão: uma que contenha
# 20 nomes e outra que contenha 20 sobrenomes.
# Cada linha do arquivo resultante deve conter um nome
# completo e a sua idade.

import random
import os
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

nomes_base = [
    "joao",
    "carla",
    "camila",
    "lucia",
    "thais",
    "helena",
    "andrea",
    "luis",
    "isac",
]

sobrenomes_base = ["silva", "leao", "machado", "mota", "de assis", "carvalho"]

with open(path.join(BASE_DIR, "data.txt"), "w") as file:
    for i in range(5):
        idade = random.randint(20, 45)
        indice_nome = random.randint(0, len(nomes_base) - 1)
        indice_sobrenome = random.randint(0, len(sobrenomes_base) - 1)

        file.write(
            f"{nomes_base[indice_nome]} {sobrenomes_base[indice_sobrenome]} com {idade} anos\n"
        )
