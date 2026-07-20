# Meio dificil, tentei aplicar todos os AND, Or e NOT de primeira.
Nome = input("Digite seu nome: ")
idade = int(input ("Coloque sua idade: "))
medico = input("Você tem um atestado médico? s para sim e n para não: ")
academia = input("Você está suspenso da academia? s para sim e n para não:  ")
vip = input("Você é aluno vip? s para sim e n para não: ")


if idade >= 16 and not academia == "s" and (medico == "s" or vip == "s" ):
    print("Acesso liberado!")
else:
    print("Não está liberado")
print(
    f"{idade}\n"
    f"{medico}\n"
    f"{academia}\n"
    f"{vip}\n")
