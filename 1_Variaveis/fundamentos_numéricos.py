#Aprendendo tudo, faço faculdade então ja tenho facilidade em entender esses passos, porém por via das dúvidas.

# Usando Int

idade = input("coloque sua idade: ") 
numero = int(idade)
print(f"Sua idade é {numero}.")


# Usando float


altura = input ("Digite sua altura: ")
numeroAL = float(altura)
peso = input("Digite seu peso: ")
numeroPE = float(peso)
print(f"Sua altura é {numeroAL} e seu peso é {numeroPE} quilos ")

# ja tava usando né mas vai str

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")
print(f"seu nome: {nome} e sua cidade: {cidade}.")

# Usando booleana, vou usar de idade que ja existe aq mesmo


maior = numero >= 18
if maior:
    print("É maior de idade.")
else:
    print("É menor de idade.")

# Tudo junto

print(f"Nome: {nome}")
print(f"Idade: {numero}")
print(f"Cidade: {cidade}")
print(f"Altura: {numeroAL}")
if maior:
    print("É maior de idade.")
else:
    print("É menor de idade.")
