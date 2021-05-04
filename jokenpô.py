from random import choice

pedra = 1
papel = 2 
tesoura = 3 

lista = [pedra, papel, tesoura]
computador = choice(lista)

print('\033[1;31m-=-=-JOKENPÔ-=-=-')
print('\033[1;97mEscolha entre:\n [ 1 ] Pedra 👊\n [ 2 ] Papel🖐️\n [ 3 ] Tesoura ✌️')

jogador = int(input('\nQual você escolhe? '))

if jogador == 1:
    
    if computador == 1:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Pedra 👊')
        print('O computador jogou Pedra 👊')
        print('-' * 30)
        print('\033[1;33mEmpatou\033[m\n')
    
    elif computador == 2:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Pedra 👊')
        print('O computador jogou Papel 🖐️')
        print('-' * 30)
        print('\033[1;31mO computador venceu\033[m\n')
        
    elif computador == 3:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Pedra 👊')
        print('O computador jogou Tesoura ✌️')
        print('-' * 30)
        print('\033[1;32mO jogador venceu\033[m\n')

elif jogador == 2:
    
    if computador == 1:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Papel 🖐️')
        print('O computador jogou Pedra 👊')
        print('-' * 30)
        print('\033[1;32mO jogador venceu\033[m\n')
    
    elif computador == 2:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Papel 🖐️')
        print('O computador jogou Papel 🖐️')
        print('-' * 30)
        print('\033[1;33mEmpatou\033[m\n')
    
    elif computador == 3:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Papel 🖐️')
        print('O computador jogou Tesoura ✌️')
        print('-' * 30)
        print('\033[1;31mO computador venceu\033[m\n')

elif jogador == 3:

    if computador == 1:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Tesoura ✌️')
        print('O computador jogou Pedra 👊')
        print('-' * 30)
        print('\033[1;31mO computador venceu\033[m\n')

    elif computador == 2:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Tesoura ✌️')
        print('O computador jogou Papel 🖐️')
        print('-' * 30)
        print('\033[1;32mO jogador venceu\033[m\n')

    elif computador == 3:
        print('\033[1;31mJO \nKEN \nPÔ!\033[m')
        print('\033[1;97m-' * 30)
        print('O jogador jogou Tesoura ✌️')
        print('O computador jogou Tesoura ✌️')
        print('-' * 30)
        print('\033[1;33mEmpatou\033[m\n')