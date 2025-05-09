"""
Programa para ler o texto de um ficheiro e copiar o mesmo para um novo
"""
import os

NOME_FICHEIRO="ficheiroA.txt"
with open(NOME_FICHEIRO,"r",encoding="utf-8")as f:
    if os.path.exists(NOME_FICHEIRO)==False:
        print("este ficheiro não existe")
    else:
        linhas=f.readlines()
with open(NOME_FICHEIRO,"a",encoding="utf-8")as f2:
    for i in range (len(linhas),-1,-1,-1):
        if linhas[i][len(linhas[i])-1]!="/n":
            linhas[i]+="/n"
        f.write(linhas[i])
        print(linhas)