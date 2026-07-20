# Esse foi mais tranquilo AND é fácil de dominar agora que entendi
nome = input("Digite seu nome: ")
idade = int(input("coloque sua idade: "))
altura = float(input("Coloque sua altura: "))
empregado = input("Está empregado? Use s para sim e n para não: ")

if idade >= 18 and empregado == "s":
    print("Pode financiar.")
elif idade >= 18 and empregado == "n":
    print("Maior de idade, mas sem renda")
else: 
    print("Menor de idade.")

if empregado == "s":
    empregado_texto = "Sim"
else:
    empregado_texto = "Não"

print(
f"Nome: {nome}\n"
f"Idade: {idade}\n"
f"Altura: {altura}\n"
f"Tem emprego? {empregado_texto}\n"
)
