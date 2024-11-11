'''
Entre com 2 números
manualmente e mostre a
soma deles na tela
'''

print("---[ INFORME OS DOIS NÚMEROS PARA SOMA ]---")
n1 = input("Digite o 1º número: ")
n2 = input("Digite o 2º número: ")

'''
Felipe explicou que quando você não converte a 
string para inteiro ou float, você na verdade
que você esta somente concatenando!

s = n1 + n2
exemplo: n1 = 1 n2 = 2
resultado: 12
'''

# Converter as strings
# + -  * /
n1 = int(n1)
n2 = int(n2)

resultado = n1 + n2

print("Resultado final: ", resultado)

