print('===== Bem vindo a boletim =======')
aluno = input('Digite o nome do aluno: ')
n1 = int(input('Nota 1Trimestre: '))
n2 = int(input('Nota 2Trimestre: '))
n3 = int(input('Nota 3Trimestre: '))
n4 = int(input('Nota 4Trimestre: '))
media = (n1 + n2 + n3 + n4) / 4

print('Olá {},  \n sua média é: {}'.format(aluno, media))