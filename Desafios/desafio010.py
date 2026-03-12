# Criei um programa que leia quanto dinehiro uma pessoa tem na carteira e mostre quantos Dólar ela pode comprar import decimal

v = float(input('Digite um valor que você tem: '))
dolar = 5.14
conversor = round(v/dolar,2)
print('Seu saldo é: R$ {} \n Total que poderá comprar de dólar é: $ {}'.format(v, conversor))
