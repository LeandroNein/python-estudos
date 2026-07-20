# ESSE FOI MUITO DIFICIL mas deu

nome = input("Escreva seu nome: ")
idade = int(input("Informe sua idade: "))
ingresso = input("Você tem um ingresso? s para Sim e n para Não: ")
acompanhado = input("Você está acompanhada? s para Sim e n para Não: ")
if idade >= 18 and ingresso == "s":
    status ="Entrada liberada."
elif idade < 18 and ingresso == "s" and acompanhado == "s":
    status ="Entrada permitida com acompanhante."
elif ingresso == "n":
    status ="Entrada negada."
else:
    status ="Procure a organização."


if ingresso == "s":
    ingresso = "Sim"
else:
    ingresso = "Não"

if acompanhado == "s":
    acompanhado = "Sim"
else:
    acompanhado = "Não"

print(f"""
    Nome: {nome}.
    Idade: {idade}.
    Ingresso: {ingresso}.
    Acompanhado: {acompanhado}

    Status:
    {status}

    """)