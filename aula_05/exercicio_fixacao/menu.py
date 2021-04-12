from alunos import insert, fetch


def mainmenu():
    print('Menu do sistema:')
    print('1. Registrar aluno')
    print('2. Buscar aluno')

    option = input('informe a opção desejada: ')

    if option == '1':
        insert()
    elif option == '2':
        fetch()
    else:
        print('fim')
