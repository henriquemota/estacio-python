# 3. Escreva um script python que receba do usuário os seguintes dados de
# aluno: matrícula, nome, ano de ingresso, escore atual e grave as
# informações em um arquivo texto com os valores de cada aluno em
# linhas distintas separados por “;”.

import os
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
with open(path.join(BASE_DIR, "data.txt"), "a") as file:
    opcao = "0"
    while opcao == "0":
        matricula = input("informe sua matricula: ")
        nome = input("informe seu nome: ")
        ano = input("informe seu ano de ingresso: ")
        escore = input("informe seu escore no curso: ")
        file.write(f"{matricula};{nome};{ano};{escore}\n")
        opcao = input("informe 1 para sair ou 0 para continuar")
