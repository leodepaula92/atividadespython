# Desenvolva um programa que leia duas notas de um alun. calcule e mostre a media

n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))

result = (n1 + n2)/2
print('Primeira Nota: {:.1f}'.format(n1))
print('Segunda Nota: {:.1f}'.format(n2))
print('Resultado da Média: {:.1f}'.format(result))