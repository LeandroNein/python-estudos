frase = input("Mande uma frase: ")
while True:
    print("""
    Digite qualquer um desses comandos para transformar sua frase!
    1 - Maiúsculo
    2 - Minúsculo
    3 - Trocar espaços por -
    4 - Procurar uma palavra
    5 - Trocar uma palavra por outra
    6 - Limpar seu texto
    7 - Sair     
          """)
    consulta = int(input("Escreva seu número: "))
    if consulta == 1:
        print(f"Sua frase em Maiúsculo: {frase.upper()}")
    elif consulta == 2:
        print(f"Sua frase em Minúsculo: {frase.lower()}")
    elif consulta == 3:
        print(f"""Sua frase com espaços trocados por "-" : {frase.replace(" " , "-")}""")        
    elif consulta == 4:
        palavra = input("Digite a palavra que deseja encontrar: ")
        posicao = frase.find(palavra)
        if posicao != -1:
            print(f"A palavra: {palavra} existe e está na posição: {posicao}.")
        else:
            print("Não achei a palavra.")
    elif consulta == 5:

        antigapalavra = input("Qual palavra você quer substituir: ")
        novapalavra = input("Digite a nova palavra: ")

        novaposicao = frase.find(antigapalavra)

        if novaposicao != -1:
            frase = frase.replace(antigapalavra , novapalavra)
            print(f"Trocando fica assim: {frase}")
        else:
            print("Não consegui achar")

    elif consulta== 6:
        if frase == "":
            print("Você ja não tem um texto.")
        else:
            certeza = input("Você tem certeza que quer apagar seu texto? s para Sim e n para Não: ").lower()
        if certeza == "s":
            frase = ""
            print("Seu texto foi limpo com sucesso")
        else:
            print("Não alterado.")
    elif consulta == 7:
        print("Adeus :D")
        break
    
    else:
        print("Não consegui o número.")

# py maisumcomloop.py