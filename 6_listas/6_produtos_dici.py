produtos = []
nomepro = input("Digite o nome do produto: ")
preco = float(input("Digte quanto o produto custa: "))
estoque = input("Digite quantos tem no estoque: ")

produto = {
    "nome": nomepro,
    "preco": preco,
    "estoque": estoque
}
produtos.append(produto)
print(produtos)


# py 6_produtos_dici.py