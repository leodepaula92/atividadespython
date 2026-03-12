# Calcule um programa que leia umnúmero inteiro Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um numero: 3.127
# O numero 6.127 tem a parte inteira 6.
from math import trunc

valor = float(input('Digite um numero: '))
# int(valor) função nativa
input('O número: {} tem a parte inteira é: {}'.format(valor, trunc(valor)))
