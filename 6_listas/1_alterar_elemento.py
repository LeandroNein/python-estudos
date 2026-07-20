# exercicio 1,2 e 3 juntos

print("Quantos produtos você quer informar?")
lista = []
produtos = int(input(""))
for i in range(1, produtos + 1):
    novo = input(f"Diga o {i} produto: ")
    lista.append(novo)

print(lista)

print("Escreva qual produto você quer substituir sabendo que se conta da esquerda pra direita e começa por 0 ")
sub = int(input(""))
prosub = input("Escreva o nome do produto novo: ")
lista[sub] = prosub
print(lista)

print("Diga um item que você deseja apagar: ")
reproduto = input("")
lista.remove(reproduto)
print(lista)

#py alterar_elemento.py