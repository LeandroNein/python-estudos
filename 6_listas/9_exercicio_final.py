print("Quantos usuários serão cadastrados?")
numero = int(input())

lista = []

for i in range(1, numero + 1):
    nome = input(f"Qual nome do usuário {i}: ")
    idade = int(input(f"Qual idade do usuário {i}: "))
    profissao = input(f"Qual a profissão do usuário {i}: ")

    usuarios = {
        "Nome": nome,
        "Idade": idade,
        "Profissão": profissao
    }

    lista.append(usuarios)

print("\nUsuários cadastrados:")

for usuario in lista:
    print(usuario["Nome"], "-", usuario["Profissão"])



# py 9_exercicio_final.py