# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar. Sabendo que o carro custa 60 por dia e R$ 0.15 por Km Rodado
print('========== Aluguel de Carros ========')
dias = int(input('Quantos dias carro ficou alugado?:'))
km = float(input('Quantos km rodados?:'))
totaldias = dias * 60
totalkm = km * 0.15
soma = totaldias + totalkm
print('Total a pagar é: R$ {:.2f} '.format(soma))
print('========== Demonstrativo =============')
print('Total de {} dias = R$ {:.2f}'.format(dias,totaldias))
print('Total de {} km Rodados = R$ {:.2f}'.format(km,totalkm))
print('======================================')
