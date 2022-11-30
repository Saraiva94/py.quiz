print("Seja bem vindo ao quiz da Equipe The Warriors! ")
print("UNIGRANRIO (EAD)")
print()
print()
print("Nomes dos criadores do jogo , no modelo Quiz")
print("[Anderson da Silva Pinto] Mat: 5406220 ")

print("[Swamiy Saraiva G. de Campos] Mat: 5406236 ")
print()
print()
print()
print("PCA Introdução ao Desenvolvimento de Sistemas")
print("APLICAÇÃO PRÁTICA")
print()
print()
print()

print("Tema: Educação")
print("Tema do jogo: COPA DO MUNDO")
print()
print('-=-' * 15)
print()
pontos = 0




while True:
    jogo_do_quiz = input("Quer começar? (S/N) : ").upper()
    if jogo_do_quiz == "S":
        print('Então prepare-se')
        break
    elif jogo_do_quiz == "N":
        print('Fim do Game...')
        exit()
        break
    else:
        print('Opção errada, tente novamente...')

print()
print('-=-' * 15)
print()

print('O JOGO  VAI COMEÇAR!!!!!'
      "________________instruções do sistema__________________"
      'Responda: as perguntas com as seguinte opções (a),(b) ou (c)')

perguntas = {

 'Pergunta 1': {
    'pergunta': 'De quem foi o gol mais rápido da história da Copa do Mundo?feito em apenas 11 segundos de jogo',
    'respostas': {'a': ' Vaclav Masek (pela Tchecoslováquia x Iugoslávia) em 1962',
                  'b': 'Hakan Sukur (pela Turquia x Coreia) em 2002',
                  'c': 'Mathias Jorgensen (pela Dinamarca x Croácia) em 2018', },
    'resposta_certa': 'b',
 },

 'Pergunta 2': {
        'pergunta': 'Quem foi o maior artilheiro da história da Copa do Mundo?',
        'respostas': {'a': 'Ronaldo ',
                      'b': 'Pelé',
                      'c': 'Miroslav Klose (Alemanha)', },
        'resposta_certa': 'c',
},
 'Pergunta 3': {
        'pergunta': 'Quem é o maior artilheiro que fez mais gols em uma das  edições da copa?',
        'respostas': {'a': 'Just Fontaine(França)',
                      'b': 'Miroslav Klose (Alemanha)',
                      'c': 'Ademir de Menezes (Brasil)', },
        'resposta_certa': 'a',
},
 'Pergunta 4': {
        'pergunta': 'Qual é a seleção com mais vices na Copa do Mundo?',
        'respostas': {'a': 'Itália',
                      'b': 'Alemanha',
                      'c': 'Brasil', },
        'resposta_certa': 'b',
},
 'Pergunta 5': {
        'pergunta': 'Qual é a única seleção presente na Copa de 2022 que nunca perdeu para o Brasil?',
        'respostas': {'a': 'Qatar',
                      'b': 'Equador',
                      'c': 'Senegal', },
        'resposta_certa': 'c',
},
 'Pergunta 6': {
        'pergunta': 'Quantos Títulos tem  a França?',
        'respostas': {'a': '2',
                      'b': '3',
                      'c': '1', },
        'resposta_certa': 'a',
},
 'Pergunta 7': {
        'pergunta': 'Quantos Títulos tem a Argentina?',
        'respostas': {'a': '3',
                      'b': '2',
                      'c': '1', },
        'resposta_certa': 'b',
},
 'Pergunta 8': {
        'pergunta': 'Quantos Títulos tem  o Uruguai?',
        'respostas': {'a': '2',
                      'b': '0',
                      'c': '3', },
        'resposta_certa': 'a',
},
 'Pergunta 9': {
        'pergunta': 'Quantos Títulos tem Itália ?',
        'respostas': {'a': '5',
                      'b': '3',
                      'c': '4', },
        'resposta_certa': 'c',
},
 'Pergunta 10': {
        'pergunta': 'Quantas Copas Pelé foi campeão junto á seleção brasileira?',
        'respostas': {'a': '4',
                      'b': '3',
                      'c': '2', },
        'resposta_certa': 'b',
},
 'Pergunta 11': {
        'pergunta': 'Qual foi a maior goleada que o Brasil já sofreu pela copa do mundo?',
        'respostas': {'a': '7a1',
                      'b': '5a0',
                      'c': '8a1', },
        'resposta_certa': 'a',
},
 'Pergunta 12': {
        'pergunta': 'Em qual seleção que o  meio-campista Deco jogou pela na Copa do mundo de 2006?',
        'respostas': {'a': 'Uruguai',
                      'b': 'Brasil',
                      'c': 'Portugal', },
        'resposta_certa': 'c',
},
 'Pergunta 13': {
        'pergunta': 'Quantos títulos Ronaldo Fenômeno ganhou pela seleção do Brasil na Copa do Mundo?',
        'respostas': {'a': '1',
                      'b': '2',
                      'c': '3', },
        'resposta_certa': 'b',
},
 'Pergunta 14': {
        'pergunta': 'Qual foi o ano da primeira Copa do Mundo?',
        'respostas': {'a': '1830',
                      'b': '1920',
                      'c': '1930', },
        'resposta_certa': 'c',
},
 'Pergunta 15': {
        'pergunta': 'Quantas Copas do Mundo o jogador Neymar ganhou?',
        'respostas': {'a': '2',
                      'b': '1',
                      'c': '0', },
        'resposta_certa': 'c',
},
 'Pergunta 16': {
        'pergunta': 'Qual foi a Seleção que ganhou a primeira Copa do Mundo?',
        'respostas': {'a': 'Argentina',
                      'b': 'Inglaterra',
                      'c': 'Uruguai', },
        'resposta_certa': 'c',
},
 'Pergunta 17': {
        'pergunta': 'Qual foi a última Seleção que Venceu uma Copa?',
        'respostas': {'a': 'Alemanha',
                      'b': 'Itália',
                      'c': 'França', },
        'resposta_certa': 'c',
},
 'Pergunta 18': {
        'pergunta': 'Qual foi a Seleção que ficou de fora da Copa de 2022 e que tem 4 Títulos',
        'respostas': {'a': 'Alemanha',
                      'b': 'França',
                      'c': 'Itália', },
        'resposta_certa': 'c',
},
 'Pergunta 19': {
        'pergunta': 'Qual é a seleção que  mais jogou em quantidade de partidas pela copa do mundo?',
        'respostas': {'a': 'Brasil',
                      'b': 'Alemanha',
                      'c': 'Itália', },

        'resposta_certa': 'b',
},
 'Pergunta 20': {
        'pergunta': 'Qual foi a seleção que participou de todas as copas?',
        'respostas': {'a': 'Brasil',
                      'b': 'Alemanha',
                      'c': 'Argentina', },
        'resposta_certa': 'a',
},
}
print()

resposta_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('respostas: ')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    print('-=-' * 15)

    if resposta_usuario == pv['resposta_certa']:
        pontos = pontos + 0.5
        print(f'voce ganhou 0.5 pela resposta certa!!{pontos} de pontos acumulados')
        print('EHHHHHHHH!!!!!ACERTOU!!!!!')
        resposta_certas += 1
        print()

    else:
        print('IXIIIII!!!! Você ERROU!!!!')
        print()

if pontos >= 5.5:
        print(f'Parabéns!! voce tem um ótimo conhecimento de todas as Copas passadas !!!!!')

elif pontos <= 5.5:
        print(f'vishiiii da próxima vez usa o google , voce nao foi bem!!!!')




print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certas / qtd_perguntas * 100


print(f'você acertou {resposta_certas} /20 das perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
print(f'sua nota final é: {pontos}')
