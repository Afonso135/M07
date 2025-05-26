"""
Programa vai ler  um ficheirio pickle e mostrar todos os  dados
"""
import pickle

with open("so_um.dat","rb") as f:
    while True:
        try:
            dados=pickle.load(f)
            print(dados)
        except EOFError:
            break
    