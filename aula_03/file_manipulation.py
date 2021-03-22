import os
from os import path

print("arquivo corrente: ", __file__)
print("caminho absoluto: ", path.abspath(__file__))
print("nome do arquivo: ", path.basename(__file__))
print("nome do arquivo (em branco): ", path.basename("/Users/henriquemota/"))
print("string em branco: ", path.basename("/Users/henriquemota/"))
print("nome do diretório: ", path.dirname(__file__))
print("diretório existe: ", path.exists("/Users/henriquemota/"))
print("caminho absoluto: ", path.isabs(__file__))
print("é arquivo?'': ", path.isfile(__file__))
print("é diretório?: ", path.isdir(__file__))
print("é link simbólico?: ", path.islink(__file__))
BASE_DIR = path.join(path.dirname(__file__), "..", "aula_02")
print("diretório: ", BASE_DIR)
