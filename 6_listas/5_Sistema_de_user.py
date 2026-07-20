lista = []
while True:
    print (""" Escolha uma das opções para fazer as ações:

        1 - Cadastrar novo usúario.
        2 - Remover usúarios.
        3 - Verificar se usúario já está cadastrados.
        4 - Contar quantos usúarios existem.
        5 - Limpar usúarios.
        6 - Ver usúarios registrados.
        7 - Sair.
    """)
    numero = int(input(""))
    if numero == 1:
        nome = input("Insira um nome: ")
        if nome in lista:
           print("Este nome já está registrado.")
        else:   
            lista.append(nome)
            lista.sort()
            print("Registro salvado com sucesso!")
    elif numero == 2:
        if not lista:
            print("OPA! Você não tem usúarios. Adicione usando 1")
        else:
            print(lista)
            remover_usu = input("Qual usúario você deseja apagar?  ")
            remover_usu = remover_usu.strip()
            if remover_usu in lista:
                tem_certeza = input(f"Tem certeza que deseja apagar o cadastro {remover_usu}? Digite Sim ou Não   ").lower()
                tem_certeza = tem_certeza.replace("á", "a")
                tem_certeza = tem_certeza.replace("à", "a")
                tem_certeza = tem_certeza.replace("ã", "a")
                tem_certeza = tem_certeza.replace("â", "a")
                if tem_certeza == "sim":
                    lista.remove(remover_usu)
                    lista.sort()
                    print(lista)
                    print("Usúario apagado.")
                elif tem_certeza == "nao":
                    print(lista)
                    print("Usúario não apagado.")
                else: 
                    print("Sua resposta foi diferente de sim ou não. Procedimento interrompido.")
            else: 
                print("Não achei esse Usúario.")
    elif numero == 3:
        pesquisa = input("Coloque o nome para pesquisar se ele ja existe: ")
        if pesquisa in lista:
            print("Ele está na lista!")
        else:
            print(f"O usúario: {pesquisa} não está na lista.")
    elif numero == 4:
        print("Quantidade de usúarios: ")
        print (len(lista)) 
        
    elif numero == 5:
        if not lista:
            print("OPA! Você não tem usúarios. Adicione usando 1")
        else:
            print(lista)
            tem_certeza_dois = input(f"Tem certeza que deseja apagar todos os usúarios? Digite Sim ou Não   ").lower()
            tem_certeza_dois = tem_certeza_dois.replace("á", "a")
            tem_certeza_dois = tem_certeza_dois.replace("à", "a")
            tem_certeza_dois = tem_certeza_dois.replace("ã", "a")
            tem_certeza_dois = tem_certeza_dois.replace("â", "a")
            if tem_certeza_dois == "sim":
                lista = []
                print(lista)
                print("Usúarios apagados.")
            elif tem_certeza_dois == "nao":
                print(lista)
                print("Usúarios não apagados.")
            else: 
                print("Sua resposta foi diferente de sim ou não. Procedimento interrompido.")
    elif numero == 6:
        if not lista:
            print("Não há usúarios registrados.")
        else:
            lista.sort()
            print(lista)
    elif numero == 7:
        print("Adeus :)")
        break
    else:
        print("Não achei esse número.")





# 5_Sistema_de_user.py