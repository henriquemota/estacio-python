import os
from os import path

BASE_DIR = path.join(path.dirname(__file__), "files")
file = open(path.join(BASE_DIR, "names.txt"))

linhas = file.readlines()
for linha in linhas:
    print(linha.strip())
    # strip remove os caracteres especiais
    # da frente e do fim da string

file.close()
