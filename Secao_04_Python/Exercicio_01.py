# Exercício 1 - Número Maior

print('---[ Informe os números abaixo ]---')
num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))

if  num1 > num2:
    print("1º Número é maior que o 2º Número: " + "1º Número: " + str(num1))
elif num2 > num1:
    print("2º Número é maior que o 1º Número: " + "2º Número" + str(num2))
else:
    print("Os números são iguais")