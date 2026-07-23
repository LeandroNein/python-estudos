nome = input("Escreva seu nome: ")
idade = input("Escreva sua idade: ")
usuarios = {
    "nome": nome,
    "idade": idade
}
usuarios ["email"] = "Leandroo97555@gmail.com"
usuarios ["telefone"] = "111111111111"


print(usuarios["nome"])
print(usuarios["email"])
print(usuarios["telefone"])


del usuarios["email"]


for chave in usuarios:
    print(chave)

for chave in usuarios:
    print(chave, usuarios[chave])
    
# py 8_usando_dicionarios.py