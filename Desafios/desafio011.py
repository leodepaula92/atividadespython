# Faça um preograma que leia a largura e a altura de uma parede em metros, calcula e sua area e a quantidade de tinta necessário para pinta-la sabendo que cada litro de tinra pinta uma area de 2m²

print('======== Orçamento Pintura ============')
a = float(input('Qual a altura da parede em metros: '))
l = float(input('Qual a largura da parede em metros: '))
area = a*l
tinta = area/2
print('Olá sua parede tem {} m², você precisará de {} litros de tinta para pinta-la'.format(area, tinta))