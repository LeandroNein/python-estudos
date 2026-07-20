numero = int(input("Coloque a quantidade: "))
soma = 0
for nota in range(1, numero + 1):
    notas = float(input(f"Digite o número {nota}: "))
    soma = soma + notas
media = soma / numero
print(f"""
    Soma: {soma}
    Média: {media}      
    """)

