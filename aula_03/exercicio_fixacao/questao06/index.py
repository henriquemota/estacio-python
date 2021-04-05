# Escreva uma função que recebe dois nomes de arquivos e
# copia o conteúdo do primeiro arquivo para o segundo arquivo.
# Considere que o conteúdo do arquivo de origem é um texto.
# Sua função não deve copiar linhas comentadas (que começão com //).
import os
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))


def my_merge():
    ori = input('informe o nome do arquivo de origem: ')
    des = input('informe o nome do arquivo de destino: ')

    ORI_FILE = path.join(BASE_DIR, ori)
    DES_FILE = path.join(BASE_DIR, des)

    with open(ORI_FILE, 'r') as file_read:
        linhas = file_read.readlines()
        with open(DES_FILE, 'a') as file_write:
            for linha in linhas:
                if ('//' not in linha):
                    file_write.write(linha)

    print('final de processamento')


my_merge()
