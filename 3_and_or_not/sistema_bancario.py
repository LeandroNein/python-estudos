# Desafio bem tranquilo

nome = input("Coloque o nome: ")
saldo = float(input("Coloque o saldo da conta: "))
valor = float(input("Coloque o valor do saque: "))
if valor <= 0:
    print("Valor inválido.")
elif valor > saldo:
    print("Saldo insuficiente.")
elif valor >= 1000 and saldo < 5000:
    print("Saque bloqueado.\n"
    "Necessário saldo mínimo de R$5000 para saques acima de R$1000.")
else:
    saldo = saldo - valor
    print("Saque realizado com sucesso!\n"
    f"Saldo restante: {saldo}")
    