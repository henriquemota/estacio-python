# 4. Escreva um script que LEIA os dados do arquivo texto gerado na questão anterior e
# exiba no console apenas os nomes dos alunos concatenado com a frase a seguir, baseado em sua regra:
# I. “em fase de adaptação” (escore menor do que 6),
# II. “familiarizado com o curso” (escore entre 6.0 e 7.0 – intervalo fechado),
# III. “em excelência no curso” (escore maior que 7,0 e menor que 8.5)
# IV. “Nasceu para o curso” (escore acima de 8.5).

import os
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
with open(path.join(BASE_DIR, "data.txt")) as file:
    linhas = file.readlines()
    for linha in linhas:
        dados = linha.split(";")
        valor = int(dados[3])

        if valor < 6:
            print(f"{dados[1]} está em fase de adaptação")
        elif valor >= 6 and valor <= 7:
            print(f"{dados[1]} está se familiarizado com o curso")
        elif valor > 7 and valor <= 8.5:
            print(f"{dados[1]} está sem excelência no curso")
        else:
            print(f"{dados[1]} nasceu para o curso")