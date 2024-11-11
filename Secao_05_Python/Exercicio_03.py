'''
26. Exercício 3 - While com IF dentro

Exercícios repetição
3 - Escreva um programa que mostre na tela todos os
números entre 1 e 100. Um embaixo do outro, exceto a
sequência que vai de 50 a 59
'''

numero = 1

while numero <= 100:
    if numero < 50 or numero > 59:
        print(numero)
    numero = numero + 1