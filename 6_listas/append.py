numero = int(input(" Coloque quantos produtos você quer colocar na lista: "))
lista = []

for i in range(1, numero + 1):
    produto = input(f"Diga o nome do produto {i}: ")
    lista.append(produto)


if "Carlos" in lista:
    lista.remove("Carlos")

print(lista)