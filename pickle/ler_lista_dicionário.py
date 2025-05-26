"""
Leitura de um ficheiro pickle com uma lista
"""
import pickle

#lista vazia
lista2=[]

with open("lista.pkl","rb") as f:
    lista2=pickle.load(f)
print(lista2)