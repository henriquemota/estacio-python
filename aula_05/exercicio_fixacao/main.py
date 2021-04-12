import alunos
from util import clear
from database import initdb

initdb()
sair = ''


def mainmenu():
    print('Menu do sistema:')
    print('1. Registrar aluno')
    print('2. Buscar aluno')

    option = input('informe a opção desejada: ')

    if option == '1':
        alunos.insert()
    elif option == '2':
        alunos.fetch()
    else:
        print('fim')


while (sair != 'sair'):
    mainmenu()
    sair = input('digite "sair"  ou qualquer tecla para continuar.')
    clear()
