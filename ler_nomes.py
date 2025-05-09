"""
Programa para ler até ao final do ficheiro
"""
import os

NOME="nomes.txt"
# Verifica se o ficheiro existe
if os.path(NOME)==False:
    print("ficheiro não existe")

with open("nomes.txt","r",encoding="utf-8") as ficheiro:
    linhas=ficheiro.readlines()
    for linha in linhas:
        print(linha,end="")