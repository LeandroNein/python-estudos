frase = input("Informe uma frase: ")
palavra = input("Escreva uma palavra dessa frase: ")
if frase.find(palavra) != -1:
    print(f"Está palavra existe na frase e está na posição: {frase.find(palavra)}")
else: 
    print(f"Está palavra não existe na frase.")