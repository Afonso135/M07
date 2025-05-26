"""
Programa que grava um dicionário com o módulo pickle
"""
import pickle

#ler dados
nome=input("insira um nome:")
idade=int(input("insira a sua idade:"))

#criar dicionario
novo={
    "nome":nome,
    "idade":idade
}

#guardar os dados
with open("so_um.dat","ab") as f:
    #serialização
    pickle.dump(novo,f)
print("Dados adicionados")
