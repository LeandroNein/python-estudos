#Desafio mais ou menos, me confundi no na hora do (nota1 + nota2 + nota3)/3 nao tava entendo pq nao tava indo até ver que era 3 kkakaka

aluno = input("Coloque o nome do aluno: ")
nota1 = float(input("Coloque a primeira nota: "))
nota2 = float(input("Coloque a segunda nota: "))
nota3 = float(input("Coloque a terceira nota:  "))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
    print(f"Média de nota do(a) {aluno} é de {media} então: Aprovado!")
elif  media >= 5:
    print(f"Média de nota do(a) {aluno} é de {media} então: Recuperação.")
else:
    print(f"Média de nota do(a) {aluno} é de {media} então: Reprovado.")

