print("Seja bem vindo ao quiz da Equipe The Warriors! ")


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
        print('Opçao errada, tente novamente...')

print()
print('-=-' * 15)
print()

print('O jogo vai começar!!!!')

perguntas = {

 'Pergunta 1': {
    'pergunta': 'QUANTO É 2+2?',
    'respostas': {'a': '3', 'b': '4', 'c': '2', },
    'resposta_certa': 'b',
 },

 'Pergunta 2': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 3': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 4': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 5': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 6': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 7': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 8': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 9': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
        'resposta_certa': 'a',
},
 'Pergunta 10': {
        'pergunta': 'QUANTO É 10+2?',
        'respostas': {'a': '12', 'b': '8', 'c': '9', },
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
        print('EHHHHHHHH!!!!!ACERTOU!!!!!')
        resposta_certas += 1
        print()

    else:
        print('IXIIIII!!!! Você ERROU!!!!')
        print()


print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certas / qtd_perguntas * 100

print(f'você acertou {resposta_certas} /10 das perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
