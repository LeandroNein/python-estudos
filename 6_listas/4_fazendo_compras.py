lista = []
while True:
    print(""" 
        Escolha um número para realiza-las:
        1 - Adicionar produto
        2 - Remover produto
        3 - Ver carrinho
        4 - Sair
        """)
    numero = int(input(""))
    if numero == 1:
        novo_produto = input("Escreva o nome do produto que queira adicionar ao carrinho: ")
        lista.append(novo_produto)
        print("Seu produto foi adicionado com sucesso ao carrinho: ")
        print(lista)
    elif numero == 2:
        if not lista:
            print("OPA! Você não tem produtos. Adicione usando 1")
        else:
            print(lista)
            remover_produto = input("Qual produto você deseja apagar?")
            remover_produto = remover_produto.strip()
            if remover_produto in lista:
                tem_certeza = input(f"Tem certeza que deseja apagar o item {remover_produto}? Digite Sim ou Não   ").lower()
                tem_certeza = tem_certeza.replace("á", "a")
                tem_certeza = tem_certeza.replace("à", "a")
                tem_certeza = tem_certeza.replace("ã", "a")
                tem_certeza = tem_certeza.replace("â", "a")
                if tem_certeza == "sim":
                    lista.remove(remover_produto)
                    print(lista)
                    print("Produto apagado! Compre mais depois :)")
                elif tem_certeza == "nao":
                    print(lista)
                    print("Produto não apagado da lista.")
                else: 
                    print("Sua resposta foi diferente de sim ou não. Procedimento interrompido.")
            else: 
                print("Não achei esse produto.")
    elif numero == 3:
        if lista == []:
            print("Seu carrinho está vazio!")
        else: 
            print(f"Aqui está seus produtos:{lista} ")
    elif numero == 4:
        print("Adeus :)")
        break
    else:
        print("Não achei esse número.")

# py 4_fazendo_compras.py