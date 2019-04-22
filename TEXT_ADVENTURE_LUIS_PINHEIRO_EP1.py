#EP1-2019: Escape Insper

#Aluno:
#Luís Eduardo Satou Ferreira Pinheiro - luisesfp@al.insper.edu.br

'''
Escape Insper
O objetivo deste Text Adventure é encontrar o professor Raulzao e pedir um adiamento do EP1.

Boa sorte!
'''

import random
import time

game_over = False
vida_jogador = 100
vida_Raulzao = 100
vida_InsperBoy = 25
vida_unicornio = 25
ajuda_do_ninja = 0
vitoria_Raulzao = False
vitoria_InsperBoy = False
pink_floyd = 0
pao_de_queijo = 0
camisa_preta = 0
cerveja = 0
carteira = 100

print('')
print('Bem vindo....')

def vitoria(jogo):
    if jogo == True:
        print('Você Venceu!!!')
        time.sleep(0.3)
        print('Você não é LEIGO!')
        time.sleep(0.3)
        print('Está de PARABÉNS!!!')
        return 'Você é O CARA!!!'
    
def morte(game_over):
    if game_over == True:
        print('Você PERDEU!!!')
        time.sleep(0.3)
        print('Você é LEIGO!!!')
        time.sleep(0.3)
        print('Perdedor!')
        return 'GAME OVER!'
    
jogador = input('Digite o nome do seu jogador: ')
print('')
time.sleep(0.2)
print('Bem vindo, {0}, ao Escape Insper!'.format(jogador))
time.sleep(0.7)
print('Como o jogo funciona:')
time.sleep(0.3)
print('Você é um aluno do insper que estava viajando e agora tem pouco tempo para terminar o EP1.')
time.sleep(0.2)
print('Então, você vai tentar falar com o professor para pedir um adiamento')
time.sleep(0.5)
print('Boa sorte na sua jornada, {0}!'.format(jogador))

