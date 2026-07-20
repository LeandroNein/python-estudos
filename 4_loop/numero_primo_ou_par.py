numero = int(input("Digite um numero para ver se é primo: "))

primo = True
if numero == 2:
    primo
elif numero == 1:
    primo = False
else:


    for i in range(2, numero, 1):
        resultado = numero % i
        if resultado == 0:
            primo = False
            break
if primo:
    print("É primo")
else:
    print("Não é primo")



#  py lembrando_for3.py