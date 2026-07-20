print("Quantas notas deseja informar?")
notas = int(input(""))
lista = []
for i in range(1, notas + 1):
    nota = float(input(f"Informe a nota {i}: "))
    lista.append(nota)

print(f"Todas as notas: {lista}")
lista.sort()
print(f"Notas em ordem: {lista}")
print(f"A menor nota: {lista[0]}")
tempo = lista.pop()
print(f"A maior nota: {tempo}")
lista.append(tempo)

# py 3_Lista_de_notas.py