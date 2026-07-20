notas = int(input("Quantas notas deseja informar? "))
soma = 0
for nota in range(1, notas + 1):
    resultado = float(input(f"Digite a nota de numero {nota}: "))
    print(f"Nota {nota}: {resultado}")
    soma = soma + resultado
media = soma/notas
print(f"media final: {media:.2f}")

#  py usando_for3.py   

# resultado = 7
# soma = 3