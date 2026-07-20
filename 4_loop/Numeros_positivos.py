numero = int(input("Digite um numero: "))
for i in range(1, numero):
    positivo = int(input(f"digite o próximo numero {i}: "))
    
    if positivo > 0:
        print(f"{positivo} Positivo")
    else:
        print("")