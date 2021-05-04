from random import randint
from time import sleep

opçoes = (' ', 'Pedra 👊', 'Papel 🖐️', 'Tesoura ✌️')
computador = randint(1, 3)

print('\033[1;31m-=-=-JOKENPÔ-=-=-')
print(computador)
print('\033[1;97mEscolha entre:\n [ 1 ] Pedra 👊\n [ 2 ] Papel🖐️\n [ 3 ] Tesoura ✌️')
jogador = int(input('\nQual você escolhe? '))
print('\033[1;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('\033[1;97m-' * 30)
print('O jogador jogou {}'.format(opçoes[jogador]))
print('O computador jogou {}'.format(opçoes[computador]))
print('\033[1;97m-' * 30)

if jogador == 1:
    
    if computador == 1:
        print('\033[1;93mEmpatou\033[m\n')
    
    elif computador == 2:
        print('\033[1;31mO computador venceu\033[m\n')
        
    elif computador == 3:
        print('\033[1;32mO jogador venceu\033[m\n')

elif jogador == 2:
    
    if computador == 1:
        print('\033[1;32mO jogador venceu\033[m\n')
    
    elif computador == 2:
        print('\033[1;93mmEmpatou\033[m\n')
    
    elif computador == 3:
        print('\033[1;31mO computador venceu\033[m\n')

elif jogador == 3:

    if computador == 1:
        print('\033[1;31mO computador venceu\033[m\n')

    elif computador == 2:
        print('\033[1;32mO jogador venceu\033[m\n')

    elif computador == 3:
        print('\033[1;93mEmpatou\033[m\n')