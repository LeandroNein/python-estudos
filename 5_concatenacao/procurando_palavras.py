frase = input("Informe uma frase: ")
palavra = input("Informe qual palavra você quer que eu busque na frase: ")
procura = frase.find(palavra)
if frase.find(palavra) != -1:
    print(f"Palavra: {palavra} foi encontrada e está na posição: {procura} ")
else: 
    print("Não achei a palavra na frase")

# py testeobemaisdiff.py