
lista = []
while True:
    print(""" 
    1 - Cadastrar contato
    2 - Procurar contato
    3 - Remover contato
    4 - Mostrar todos
    5 - Sair
    """)
    numero = int(input(""))

    if numero == 1:
        print("Quantos contatos quer cadastrar? Escreva apenas o número de usúarios!")
        quantos_usuarios = int(input(""))
        if quantos_usuarios > 0:
            for i in range(1, quantos_usuarios + 1):
                nome = input(f"Diga o nome do usúario {i}: ")
                nome = nome.strip()
                email = input(f"Diga o email do usúario {i}: ")
                email = email.strip()
                if email.find("@") != -1:
                    telefone = input(f"Diga o número do usuário {i}: ")
                    telefone = telefone.strip()
                    telefone = telefone.replace("-", "")
                    telefone = telefone.replace("(", "")
                    telefone = telefone.replace(")", "")
                    telefone = telefone.replace(" ", "")

                    usuarios = {
                        "nome": nome,
                        "email": email,
                        "telefone": telefone
                    }

                    lista.append(usuarios)
                    print("Usuário registrado com sucesso!")
                else:
                    print("O email não é válido.")
        else:
            print("Número inválido.")

    elif numero == 2:
        if not lista:
            print("Registre usúarios para procura-los!")
        else:
            pesquisa = input("Digite o email para procurar se o usúario está registrado: ")
            pronto = False
            for usuarios in lista:
                if pesquisa == usuarios["email"]:
                    print("O usúario está cadastrado:")
                    print(usuarios["nome"], "-", usuarios["telefone"], "-", usuarios["email"])
                    pronto = True
                    break
            if  not pronto:
                print("Usúario não encontrado!") 


    elif numero == 3:
        if not lista:
            print("Registre usúarios para exclui-los!")  
        else:              
            remover = input("Escreva o telefone do contato deseja apagar: ")

            diff = False
            for usuarios in lista:
                if remover == usuarios["telefone"]:
                    print("Você tem certeza que deseja apagar este contato? Sim ou não?")
                    diff = True
                    resposta = input("").lower()
                    resposta = resposta.strip()
                    resposta = resposta.replace("s", "sim")
                    resposta = resposta.replace("n", "nao")
                    resposta = resposta.replace("não", "nao")
                    if resposta == "sim":
                        lista.remove(usuarios)
                    elif resposta== "nao":
                        print("Operação cancelada")
                    break
            if  not diff:
                print("Usúario não encontrado!") 
                

    elif numero == 4:
        print("Aqui está todos os usúarios: ")
        for usuarios in lista:
            print(usuarios["nome"], "-", usuarios["email"], "-", usuarios["telefone"])
    elif numero == 5:
        print("Adeus :)")
        break

    else:
        print("Não achei esse número.")
# 10_exercicio_extra.py