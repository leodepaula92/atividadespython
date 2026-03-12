# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

v = float(input('Digite um valor em Metros: '))
cm = v*100
mm = v*1000
print('Você digitou {} Metros \n Tota de: {} centimetros \n Total de: {} milimetros'.format(v, cm, mm))