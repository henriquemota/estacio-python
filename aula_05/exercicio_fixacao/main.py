import alunos
import turmas
import matriculas
from util import clear
from database import initdb

initdb()  # inicializa o banco de dados
sair = ''


def mainmenu():
    print('Menu do sistema:')
    print('1. Registrar aluno')
    print('2. Buscar aluno')
    print('3. Atualizar dados de um aluno')
    print('4. Excluir aluno')
    print('5. Registrar turmaa')
    print('6. Buscar turma')
    print('7. Atualizar dados de uma turma')
    print('8. Excluir turma')
    print('9. Matricular aluno em turma')

    option = input('informe a opção desejada: ')

    if option == '1':
        turmas.insert()
    elif option == '2':
        alunos.fetch()
    elif option == '3':
        alunos.update()
    elif option == '4':
        alunos.delete()
    elif option == '5':
        turmas.insert()
    elif option == '6':
        turmas.fetch()
    elif option == '7':
        turmas.update()
    elif option == '8':
        turmas.delete()
    elif option == '9':
        matriculas.insert()
    else:
        print('fim')


while (sair != 'sair'):
    mainmenu()
    sair = input('digite "sair"  ou qualquer tecla para continuar.')
    clear()
