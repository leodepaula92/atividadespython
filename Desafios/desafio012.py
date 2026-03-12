# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print('======== DESCONTO LIQUIDAÇÃO =========')
v = float(input('Digite um valor do produto: R$ '))
desc = v * 0.05
novopreco = v - desc
print('Valor do Produtos Atual: R$ {:.2f}\n Desconto 5% Total desconto: R$ {:.2f} \n Valor Final com desconto: R$ {:.2f}'.format(v,desc, novopreco))
