nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
cidade = input("Informe sua cidade: ")

nome = nome.strip()
cidade = cidade.strip()
nome = nome.upper()
cidade = cidade.lower()

confirmar = input("Deseja confirmar o cadastro? S para sim e N para não: ").lower()
if confirmar == "s":
    print(f"""
    ===== CADASTRO =====
    Nome: {nome}
    Idade:{idade}
    Cidade: {cidade}
    Cadastro realizado com sucesso!
    """)
elif confirmar == "n":
    print("Cadastro cancelado.")
