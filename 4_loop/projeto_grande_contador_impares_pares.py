print("Quantos números deseja informar? ")
numero = int(input(""))
soma = 0
contador_pares = 0
contador_impar = 0
for i in range(1, numero + 1):
    
    novo_numero = int(input(f"número {i}: "))

    if i == 1:
        maior = novo_numero
        menor = novo_numero

    if novo_numero > maior:
        maior = novo_numero
    elif novo_numero < menor:
        menor = novo_numero
    
    if novo_numero % 2:
        contador_impar = contador_impar + 1
         
    else:
        contador_pares = contador_pares + 1
    
    soma = soma + novo_numero

media = soma/numero


print(f"menor: {menor} maior: {maior} contador impares = {contador_impar} contador pares = {contador_pares} soma: {soma} media = {media}")


# py programa_2for.py