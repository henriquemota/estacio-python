import os
from os import path

ABS_PATH = path.abspath(__file__)  # caminho absoluto do arquivo corrente
BASE_DIR = path.dirname(ABS_PATH)  # diretorio base do arquivo corrente

BASE_DIR = path.join(BASE_DIR, "files")  # muda o diretorio para o diretorio "files"
FILE_NAME = path.join(BASE_DIR, "names.txt")  # path para o caminho do arquivo desejado

# file = open(FILE_NAME)

# strlinhas = file.read()
# print(type(strlinhas))
# print(strlinhas)

# print(file.readline().strip())
# print(file.readline().strip())

# listLinhas = file.readlines()
# print(type(listLinhas))
# for linha in listLinhas:
#     print(f"olá {linha.strip()}")

# file.close()

# with open(FILE_NAME) as file:
#     listLinhas = file.readlines()
#     for linha in listLinhas:
#         print(f"olá {linha.strip()}")


with open(FILE_NAME, "a") as file:
    # file.write("henrique\n")
    # newLines = ["andre\n", "francisco\n", "jose\n"]
    newLines = ("andre\n", "francisco\n", "jose\n")
    file.writelines(newLines)
