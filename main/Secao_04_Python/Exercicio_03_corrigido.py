num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
op = input("Digite a operação( + , - , * , / ):")

if op == '+':
    print("Resultado: " + str( num1 + num2 ))
elif op == '-':
    print("Resultado: " + str( num1 - num2 ))
elif op == '*':
    print("Resultado: " + str( num1 * num2 ))
elif op == '/':
    print("Resultado: " + str( num1 / num2 ))
else:
    print("Operador informado é invalido!")