from menu import mainmenu
from util import clear

sair = ''
while (sair != 'sair'):
    mainmenu()
    sair = input('digite "sair"  ou qualquer tecla para continuar.')
    clear()
