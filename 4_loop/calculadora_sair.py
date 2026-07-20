# py calculadora_sair.py


while True:
    operadores = input ("""Digite qual você quer:
        
        1 - Soma.
        2 - Subtração.
        3 - Multiplicação.
        4 - Divisão.
        5 - Potência.
        6 - Resto da divisão.
        7 - Divisão inteira.
        Ou digite "sair" para sair da calculadora.                  
    """)
    if operadores == "sair":
        break
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    if operadores == "1":
        print(f"{numero1 + numero2}")
    elif operadores == "2":
        print(f"{numero1 - numero2}")
    elif operadores == "3":
        print(f"{numero1 * numero2}")
    elif operadores == "4":
        if numero2 == 0:
            print("Não da pra dividir")
        else:
            print(f"{numero1 / numero2}")
    elif operadores == "5":
        print(f"{numero1 ** numero2}")
    elif operadores == "6":
        print(f"{numero1 % numero2}")
    elif operadores == "7":
        print(f"{numero1 // numero2}")
    elif operadores == "sair":
        break
    else:
        print("Não operacional")
print("saiu :D")

        