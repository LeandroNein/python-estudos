# Desafio médio, me perdi um pouco mas consegui fazer

saldo = 1200
while True:
    print(
    "Digite 1 para ver seu saldo.\n"
    "Digite 2 para depositar no seu saldo.\n"
    "Digite 3 para sacar o dinheiro do saldo.\n"
    "Digite 4 para sair do menu."
    )
    opcao = input("")
    if opcao == "1":
        print(f"Seu saldo: {saldo}") 
    elif opcao == "2":
        valor = float(input ("Digite um valor para adicionar ao seu saldo: "))
        saldo = valor + saldo
        print(f"Seu saldo: {saldo}")
        print(f"Valor adicionado: {valor}")
    elif opcao == "3":
        sacar = float(input ("Digite um valor para sacar do seu saldo: "))
        if sacar > saldo:
            print("Você não pode pegar esse valor.")
        elif sacar <= 0:
            print("Vai colocar valor que nem tem? KKKKKKKKKKKKK")
        else:
            saldo = saldo - sacar
            print(f"Valor atual: {saldo}")
            print(f"Valor retirado: {sacar}")
    elif opcao == "4":
        print("Adeus :)")
        break
    else:
        print("selecione uma das opções.")

        
    

