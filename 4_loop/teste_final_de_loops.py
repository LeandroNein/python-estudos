# Lição número Desafio 1:

# for i in range(1, 50 + 1):
#   print(i)

# Lição 2:
# for i in range(50, 0, -1):
#    print(i)

# Lição 3
# for i in range(0, 101, 5):
#   print(i)


# Desafio 2 Lógica
# exercicio 4
# numero = int(input("Escolha um número: "))
# for i in range(1, 20 + 1):
#    print(f"{numero} x {i} = {numero * i}")

# Exercicio 5

# print("Quantos números você quer digitar? ")
# numero = int (input("")) 
# soma = 0
# for i in range(1, numero + 1):
#    tudo = int(input(f"Digite o {i} numero: "))
#    if i == 1:
#        menor = tudo
#       maior = tudo
#    elif tudo >= maior:
#        maior = tudo
#    elif tudo <= menor:
#        menor = tudo
#    soma = soma + tudo
# media = soma/numero
# print(f"soma: {soma} maior: {maior}   menor: {menor} media: {media}")

# Exercício 6


# pares = True
# soma_pares = 0
# numero = int(input("Escreva um número: "))
# for i in range(1, numero + 1):
#    if numero == 1:
#        pares = False
#        soma_pares = 0
#        break
#    elif numero == 2:
#        pares = True
#        soma_pares = 1
#        break
#    else:

#        contador = i % 2
#        if contador == 0:
#            pares = True
#            soma_pares = soma_pares + 1
#        elif contador > 0:
#            pares = False

# if pares:
#    print(f"{numero} é um número par e pra chegar nele tinham: {soma_pares}")
# else:
#    print(f"{numero} é um número impar")

# Desafios de Loops reais

# Exercício 7


# senhacerta = "python123"
# senhausu = 0
# foi = True
# for i in range(4, 0, - 1):
    
#    if i == 4:
#        print("Informe sua senha corretamente para nao cair em tentativas")
#    elif senhausu != senhacerta:
#        print(f"Senha incorreta, você tem mais {i} tentativa(s)")
#    senhausu = input("Digite sua senha: ") 

#    if senhausu == senhacerta:
#        foi
#        break
#    elif i == 1:
#        foi = False


# if foi:
#    print("Bem vindo :)")

# elif foi == False:

#    print("Conta bloqueada.")


#Exercício 8


# mensagem = input("Escreva uma mensagem qualquer: ")
# while True:
#    print("""
#        Coloque o número para fazer uma das ações:
#        1 - Somar
#        2 - Multiplicar
#        3 - Ver mensagem
#        4 - Sair
#        """)
#    feito = int(input(""))

#    if feito == 1:
#        numero1 = float(input("Digite o primeiro número: "))
#        numero2 = float(input("Digite o segundo número: "))  
#        print(f"{numero1} + {numero2} = {numero1 + numero2}")
#    elif feito == 2:
#        numero1 = float(input("Digite o primeiro número: "))
#        numero2 = float(input("Digite o segundo número: ")) 
#        print(f"{numero1} x {numero2} = {numero1 * numero2}")
#    elif feito == 3:
#        print(f"Sua mensagem: {mensagem}")
#    elif feito == 4:
#        print("Adeus :C")
#        break

# positivo = 0
# zero = 0
# negativo = 0
# for i in range(1, 10 + 1):
#    numero = float(input(f"informe um número {i}: "))
#    if numero == 0:
#        zero = zero + 1
#    elif numero > 0:
#        positivo = positivo + 1
#    elif numero < 0:
#        negativo = negativo + 1
# print(f"Tem {zero} zeros, tem {positivo} positivos e {negativo} negativos")

# Nível 4 — Desafio

# Exercício 10

# numero = int(input("Mande um número: "))
# for i in range(1, numero + 1):
#    i = print("*" * numero)
    
# Exercício 11

# numero = int(input("Coloque um número: "))
# for i in range(1, numero + 1):
#    i = print("*" * numero)
#   numero = numero - 1

# Exercicio final 12

saldo = 1000
while True:
    print(""" Clique um dos números para fazer seus comandos:
        1 - Ver saldo
        2 - Depositar
        3 - Sacar
        4 - Sair
         """)
    numero = int(input(""))

    if numero == 1:
        print(f"Seu saldo é de: {saldo}")
    elif numero == 2:
        deposito = float(input("Deposite um saldo: "))
        if deposito <= 0:
            print("Você não pode fazer depósito a baixo de 0 reias")
        elif deposito > 5000:
            print("Você não pode fazer depósito a cima de 5 mil reias")
        elif deposito > 0:
            saldo = saldo + deposito
            print(f"Depósito foi aplicado! seu saldo agora é: {saldo}")
    elif numero == 3:
        saque = float(input("Deposite um saldo: "))
        if saque > saldo:
            print(f"Você não pode sacar mais do que {saldo}")
        elif saque <= 0:
            print(f"Você não pode fazer saques abaixo de 0")
        elif saque <= saldo:
            saldo = saldo - saque
            print(f"Seu saque foi feito com sucesso você agora tem: {saldo}")
    elif numero == 4:
        print("Saiu :D")
        break





# py testefinal_for.py