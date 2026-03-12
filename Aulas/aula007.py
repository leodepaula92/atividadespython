n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

#soma
soma = n1 + n2

#Subtração
subtracao = n1 - n2

#Multiplicação
multiplicacao = n1 * n2

#Divisão
divisao = n1 / n2

#Potênciação
potencia = n1 ** n2

#Divisão Inteiro
divisaointeira = n1 // n2

#Resto da Divisão
restodivisao = n1 % n2

#Ordem operação: 1. Parentes - 2. Potênciação - 3. Multiplicação, Divisão, Divisão Inteiro e Resto da Divisão - 4. Soma e Subtração
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
print('A subtracao entre {} e {} vale {}'.format(n1, n2, subtracao))
print('A multiplicação entre {} e {} vale {}'.format(n1, n2, multiplicacao))
print('A divisão entre {} e {} vale {}'.format(n1, n2, divisao))
print('Potencia entre {} e {} vale {}'.format(n1, n2, potencia))
print('Divisão inteira entre {} e {} vale {}'.format(n1, n2, divisaointeira))
print('Resto da divisão entre {} e {} vale {}'.format(n1, n2, restodivisao))