"""
Programa para ler 10 nomes e escrever num ficheiro
"""

with open("nomes.txt","w",encoding="utf-8") as ficheiro:
    nome=input("insira o seu nome:")
    ficheiro.write(nome)
    ficheiro.write("\n")
    ficheiro.close()
    