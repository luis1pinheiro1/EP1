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
vida_jogador = 175
vida_Raulzao = 100
vida_InsperBoy = 25
ajuda_do_ninja = 0
vitoria_Raulzao = False
vitoria_InsperBoy = False
pink_floyd = 0
camisa_preta = False
jogo = 0
vida_humbertao = 75
vitoria_Raulzao = False
comeu = False

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

def cenarios():
    cenario = {
        'inicio': {
            'titulo' : 'Rua Quatá',
            'chave' : 'que',
            'descricao' : 'Voce esta na Rua Quata, em frente aos dois prédios do insper.'
                          'Para qual predio deseja ir?',
            'opcoes' : {
                'predio 1' : 'entrar no predio 1',
                'predio 2' : 'entrar no predio 2',
                'sujinhus' : 'ir para o bar'
            }
        },
        'predio 2' : {
            'titulo' : 'o predio novo',
            'chave' : 'que',
            'descricao' : 'o ar condicionado esta bem frio e ha varios lugares para explorar.'
                          'Para qual lugar deseja ir?',
            'opcoes' : {
                'Toboga' : 'descer o toboga',
                'FabLab' : 'inventar alguma coisa',
                'Aquario' : 'estudar em um aquario',
                'inicio' : 'voltar para Quatá'
            }
        },
        'FabLab' : {
            'titulo' : 'A sala de invencoes',
            'chave' : 'que',
            'descricao' : 'O laboratório é cheio de apetrechos e é possível inventar varias coisas, mas você não tem criatividade pois apenas pensa em entregar o EP.'
                          'O que você quer fazer?',
            'opcoes' : {
                'predio 2' : 'sair do FabLab',
                'mesa do FabLab' : 'tentar inventar alguma coisa'
            }
        },
        'mesa do FabLab' : {
            'titulo' : 'Perca de tempo',
            'chave' : 'que',
            'descricao' : 'você não teve criatividade para inventar alguma coisa e apenas perdeu um valioso tempo do seu dia',
            'opcoes' : {
                'Acabou o tempo' : 'O projeto não pode mais ser feito'
            }
        },
        'Toboga' : {
            'titulo' : 'descida para o inferno',
            'chave' : 'que',
            'descricao' : 'Você decidiu descer o toboga, mas não esperava que te levasse diretamente para o inferno'
                          'No inferno, você descobre que o capeta poderá te dar uma chance de voltar a terra se você aceitar que não entregará o EP hoje'
                          'Claramente, você não aceita isso e o capeta te queima no inferno',
            'opcoes' : {
                'morrer' : 'não tem mais o que fazer'
            }
        },
        'Morrer' : {
            'titulo' : 'Você MORREU!',
            'chave' : 'que',
            'descricao' : 'Você está MORTO! Não tem mais o que fazer agora',
            'opcoes' : {}
        },
        'Aquario' : {
            'titulo' : 'Hora de estudar',
            'chave' : 'que',
            'descricao' : 'Você decidiu entrar no aquário para estudar e adiantar uma parte do EP. Você deseja ficar mais enérgico para fazer fazer o EP mais rápido.',
            'opcoes' : {
                'tomar redbull' : 'ir comprar na máquina',
                'ficar com sede' : 'Não consegue fazer o EP e vai para a Rua Quata',
                'inicio' : 'voltar para o inicio'
            }
        },
        'Acabou o tempo' : {
            'titulo' : 'o tempo acabou',
            'chave' : 'que',
            'descricao' : 'Você não tem mais tempo para entregar o EP. FIM DE JOGO!',
            'opcoes' : {}
        },
        'sujinhus' : {
            'titulo' : 'O bar do litrão caro',
            'chave' : 'que',
            'descricao' : 'Você decide ir ao bar tomar apenas um litrão de cerveja, mas acaba tomando 8 litros de cerveja e 7 shots de cachaça e acaba ficando embriagado e dando PT.'
                          'Você acaba perdendo tempo por beber no bar e não consegue mais fazer o EP',
            'opcoes' : {}
        },
        'predio 1' : {
            'titulo' : 'o predio onde tudo começou',
            'chave' : 'que',
            'descricao' : 'você está no saguão do predio 1 e há varios lugares para explorar',
            'opcoes' : {
                'elevador' : 'ir para o elevador e tentar achar o professor',
                'biblioteca' : 'procurar alguma ajuda',
                'pao de queijo' : 'comer um pouco',
                'inicio' : 'voltar para o inicio'
            }
        },
        'biblioteca' : {
            'titulo' : 'knowledgeland',
            'chave' : 'que',
            'descrcao' : 'biblioteca, a casa do saber! Há varias coisas para explorar',
            'opcoes' : {
                'explorar biblioteca' : 'tentar achar alguma coisa que te ajude',
                'predio 1' : 'voltar para o saguão do predio 1'
            }
        },
        'explorar biblioteca' : {
            'titulo' : 'um mundo de livros',
            'chave' : 'que',
            'descricao' : 'você não acha nada que possa te ajudar',
            'opcoes' : {
                'biblioteca' : 'voltar para a entrada da biblioteca'
            }
        },
        'pao de queijo' : {
            'titulo' : 'hora de comer',
            'chave' : 'que',
            'descricao' : 'você está com fome e quer um pao de queijo',
            'opcoes' : {
                'pao de queijo recheado' : 'comer o pao de queijo recheado',
                'predio 1' : 'voltar para o saguão do predio 1'
            }
        },
        'maquina' : {
            'titulo' : 'redbull te da raiva',
            'chave' : 'que',
            'descricao' : 'você vai comprar redbull mas a maquina engole seu dinheiro e não te dá o redbull'
                          'você tem um ataque de raiva e acaba por morrer de um subsequente ataque cardiaco',
            'opcoes' : {
                'morrer' : 'não tem mais o que fazer'
            }
        },
        'elevador' : {
            'titulo' : 'aquilo que te leva de um andar a outro',
            'chave' : 'que',
            'descricao' : 'você decide explorar o prédio para tentar fazer o EP e falar com o professor',
            'opcoes' : {
                '4 andar' : 'andar das engenharias',
                'refeitorio' : 'é melhor ir no quatá city',
                'predio 1' : 'voltar para o saguão do insper'
            }
        },
        '4 andar' : {
            'titulo' : 'o andar dos engenheiros',
            'chave' : 'que',
            'descricao' : 'este andar possui varios laboratorios, mas há apenas uma sala em que você tem aula de design de software',
            'opcoes' : {
                'sala de DesSoft' : 'arriscar tudo',
                'elevador' : 'voltar para o elevador'
            }
        },
        'refeitorio' : {
            'titulo' : 'era melhor ter ido comer no quatá city',
            'chave' : 'que',
            'descricao' : 'a comida é muito cara e você vai a falência e morre de tanto comer',
            'opcoes' : {
                'morrer' : 'nao tem mais o que fazer'
            }
        },
        'sala de DesSoft' : {
            'titulo' : ' a origem do problema',
            'chave' : 'que',
            'descricao' : 'a sala está arrumada e você vê o que parece ser o professor de costas'
                          'ao chegar perto do professor, percebe que na verdade é o demônio e ele engole sua alma e manda sua alma para o inferno',
            'opcoes' : {
                'morrer' : 'não tem mais o que fazer'
            }
        },
        'easter egg' : {
            'titulo' : 'Pink Floyd',
            'chave' : 'que',
            'descricao' : 'Você desvendou o segredo do jogo e Roger Waters aparece do nada cantando Time'
                          'Por causa desse fat inusitado , o tempo congela e você consegue fazer o EP.',
            'opcoes' : {
                'entregar EP' : 'use o computador e envie-o via github'
            }
        },
        'entregar EP' : {
            'titulo' : 'YOU DID IT!',
            'chave' : 'que',
            'descricao' : 'você conseguiu!'
            }
        }
    nome_cenario_agora = 'inicio'
    return cenario, nome_cenario_agora

cenario, cenario_agora = cenarios()

while not game_over and jogo != 200:
    cenario_agora = cenario[cenario_agora]
    easter_egg = cenario_agora['chave']
    descricao = cenario_agora['descricao']
    spawn_monstros = random.randint(1,901)
    if spawn_monstros < 65 and vitoria_Raulzao == False:
        print('Raulzao the computer boy apareceu!')
        time.sleep(0.3)
        print('o que você vai fazer com o seu professor?')
        print('opcoes: "lutar" ou "fugir" ')
        luta = input("o que fazer? - ")
        if luta == "lutar":
            print('')
            print('Raulzao tem 100 pontos de vida!')
            print('você tem {0} pontos de vida!'.format(vida_jogador))
            print('')
            while vida_jogador>0 and vida_Raulzao>0:
                attk_jogador = random.randint(15,25)
                print('você deu {0} de ataque em Raulzao!'.format(attk_jogador))
                print('')
                time.sleep(0.5)
                vida_Raulzao -= attk_jogador
                print('Raulzao tem {0} de vida!'.format(vida_Raulzao))
                print('')
                time.sleep(1)
                attk_Raulzao = random.randint(1, 18)
                print('Raulzao te deu {0} de dano'.format(attk_Raulzao))
                print('')
                time.sleep(0.5)
                vida_jogador -= attk_Raulzao
                print('você tem {0} de vida!'.format(vida_jogador))
                print('')
            if vida_jogador>0:
             print('Você derrotou raulzao e a entrega do EP será adiada!')
             print('')
             print('')
             time.sleep(1)
             vitoria_Raulzao = True
             jogo = True
            else:
               game_over = True
        else:
            print('Você voltou para o inicio')
            cenario_agora = 'inicio'
    elif spawn_monstros < 130 and camisa_preta == False:
        print('um InsperBoy de ressaca da TETTO apareceu!')
        print('o que deseja fazer? "lutar" ou "fugir"?')
        luta = input('o que fazer? - ')
        if luta =="lutar":
            print('')
            print('O InsperBoy fala que vai te chamar para um camarote na sutton e tem 25 de vida')
            print('você tem {0} de vida!'.format(vida_jogador))
            print('')
            time.slep(0.5)
            while vida_jogador>0 and vida_InsperBoy>0:
                attk_jogador = random.randint(5, 16)
                print('você deu {0} de dano no InsperBoy!'.format(attk_jogador))
                print('')
                time.sleep(1)
                attk_InsperBoy = random.randint(1,8)
                print('InsperBoy deu {0} de dano em você!'.format(attk_InsperBoy))
                print('')
                time.sleep(0.5)
                vida_jogador -= attk_InsperBoy
                print('Você tem {0} de vida!'.format(vida_jogador))
            if vida_jogador > 0:
                print('você derrotou o InsperBoy e não irá estourar o limite do cartao do papai!')
                print('')
                camisa_preta = True
            else:
                game_over = True
                
                
                

        
                
        
        
        
    


       
        
                    
     
    