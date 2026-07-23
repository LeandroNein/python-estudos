usuarios = []
print("Quantos usúarios você quer cadastrar?")
quantidade = int(input(""))


for i in range(1, quantidade + 1):

    nome = input(f"Diga o nome do usúario {i}: ")
    idade = int(input(f"Digite a idade do usúario {i}: "))
    email = input(f"Digite o email do usúario {i}: ")
    usuario = {
    "nome": nome,
    "idade": idade,
    "email": email
    }
    usuarios.append(usuario)

print(usuarios)

# py 7_cadastro_usuarios.py