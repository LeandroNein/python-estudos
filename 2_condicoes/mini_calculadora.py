# Desafio bem de boa

numero = int(input("Mande o primeiro número: "))
numerodois = int(input("Mande o segundo número: "))
operador = input("coloque um operador: ")

if operador == "*":
    print(f"Resultado: {numero * numerodois}" )
elif operador == "+":
    print(f"Resultado: {numero + numerodois}" )
elif operador == "-":
    print(f"Resultado: {numero - numerodois}" )
elif operador == "x":
    print(f"Resultado: {numero * numerodois}" )
elif operador == "/":
    print(f"Resultado: {numero / numerodois}" )
elif operador == "**":
    print(f"Resultado: {numero ** numerodois}" )
else:
    print("digite um valor valido")

