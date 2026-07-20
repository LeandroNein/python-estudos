# Desafio fácil

numero1 = float(input("Coloque o primeiro numero: "))
numero2 = float(input("Coloque o segundo numero: "))
print(
"1 - Soma\n"
"2 - Subtração\n"
"3 - Multiplicação\n"
"4 - Divisão\n"
"5 - Potência\n"
"6 - Resto da divisão\n"
"7 - Divisão inteira\n"
)
operador = int(input(""))
if operador == 1:
    print(f"Soma: {numero1 + numero2}")
elif operador == 2:
    print(f"Subtração: {numero1 - numero2}")
elif operador == 3:
    print(f"Multiplicação: {numero1 * numero2}")
elif operador == 4 and numero2 != 0:
    print(f"Divisão: {numero1 / numero2}")
elif operador == 5:
    print(f"Potência: {numero1 ** numero2}")
elif operador == 6:
    print(f"Resto da divisão: {numero1 % numero2}")
elif operador == 7:
    print(f"Divisão inteira: {numero1 // numero2}")
else:
    print("Operação inválida.")