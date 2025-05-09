"""
Programa para validar uma frase em inglês utilizando um ficheiro de texto como dicionário
"""  
import os
NOME_F="words_alpha.txt"

if os.path.exists(NOME_F)==False:
    print("Dicionário não existe")


with open(NOME_F,"r",encoding="utf8") as f:
    frase=input("insira uma frase em inglês:")
    palavras=frase.split(" ")
    #converter todas as palavras do dicionário para minúsculas
    linhas=f.readlines()
for i in range(len(linhas)):
    #remover o "/n no final daS linhas?"
    linhas[i].replace("\n","")
    """verificar se as palavras pertecem a lista do dicionárioa"""
erro=False
for palavra in palavras:
        #adicionar "/n" porque existe nas palavras do dicionário
        if palavra not in  linhas:
            print("A palavra {palavras} não existe ou está errada")
            erro=True
if erro == False:
     print("A frase não tem erros")
     