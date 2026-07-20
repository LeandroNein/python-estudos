print("Quantas notas deseja informar?")
notas = int(input(""))
soma = 0

for i in range(1, notas + 1):
    nota = float(input(f"Nota {i}: "))
    if i == 1:
        mais = nota
        menos = nota

    if nota > mais:
        mais = nota
    elif nota < menos:
        menos = nota
    
    soma = soma + nota

media = soma/notas

print(f"""
    Média: {media} 
    Maior nota: {mais}
    Menor nota: {menos}
""")

# py programa_for.py