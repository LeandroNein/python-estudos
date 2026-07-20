# Aprendi mas esse foi no esforço kakakaka
 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
convite = input("Tem convite? Digite s para sim e n para não: ")
vip = input("Esta na lista de VIPs? Digite s para sim e n para não: ")
if (vip=="s" or convite == "s") and idade >= 18:
    print("Entrada Liberada!")
else:
    print("Não pode entrar.")