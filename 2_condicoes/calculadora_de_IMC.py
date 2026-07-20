# Desafio fácil

Nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
IMC = peso / (altura ** 2)
print(f"Seu nome: {Nome}")
print(f"Seu Imc: {IMC:.2f}")

if IMC < 18.5:
    print("Você está abaixo do peso!")
elif 18.5 <= IMC < 25:
    print("Você está com peso normal!")
elif 25 <= IMC < 30.0:
    print("Você está com sobre peso!")
else:
    print("Você está obeso!")