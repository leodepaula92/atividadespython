# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo sálario com 15% de aumento.

print('======== Reajuste Salarial =========')
s = float(input('Digite o Sálario atual: R$ '))
aumento = s * 0.15
novos = s + aumento
print('Sálario Atual: R$ {:.2f} \n Aumento de 15%: R$ {:.2f} \n Novo Sálario: R$ {:.2f}'.format(s, aumento, novos))