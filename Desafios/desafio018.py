#calculo SENO, COSSENO e TANGENTE
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo: '))

seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSENO de {:.2f}'.format(angulo, coseno))
print('O angulo de {} tem TANGENTE de {:.2f}'.format(angulo, tangente))