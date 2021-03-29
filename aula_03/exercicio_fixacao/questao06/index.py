# Escreva uma função que recebe dois nomes de arquivos e 
# copia o conteúdo do primeiro arquivo para o segundo arquivo. 
# Considere que o conteúdo do arquivo de origem é um texto. 
# Sua função não deve copiar linhas comentadas (que começão com //).
import os
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

def mymerge(ori, des):
