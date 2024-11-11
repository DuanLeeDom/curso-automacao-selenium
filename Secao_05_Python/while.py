conta = -100
nvezes = 0
while conta < 0:
    print("Você esta em débito")
    print("Adicionando 10")
    conta = conta + 10
    print("Valor da conta é: " + str(conta))
    
    nvezes = nvezes + 1
    if nvezes == 3:
        break
else:
    print("Você não esta em débito!")

print("Final da Opearação!")

## break quebra a linha de repetição