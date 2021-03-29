import os
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

nome = input('informe seu nome: ')
nascimento = input('informe seu nascimento no formado YYYY/MM/DD: ')
email = input('informe seu email: ')

with open(path.join(BASE_DIR, "banco_dados.csv"), "a") as file:
    file.write(f'{nome};{nascimento};{email}\n')
