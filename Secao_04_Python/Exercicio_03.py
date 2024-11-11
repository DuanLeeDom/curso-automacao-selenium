n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

print("Operações \n1) + \n2) - \n3) * \n4) /")
op = int(input('Informe a operação: '))

if op == 1:
    resultado = n1 + n2
elif op == 2:
    resultado = n1 - n2
elif op == 3:
    resultado = n1 * n2
elif op == 4:
    resultado = n1 / n2
else:
    print('Números Iguais')


print('---[ Exibição final ]---')
print('Resultado: ' + str(resultado))