"""
Programa que utiliza o modulo pickle para guardar uma lista num ficheiro binário
"""
import pickle

#lista de dados a guardar
lista=[1,2,3,
       "quatro",
       {"nome":"cinco","email":"cinco@gmail.com"},
       6]

#guardar dados no ficheiro serializando a lista de uma vez só
with open("lista.pkl","wb")as f:
    pickle.dump(lista,f)
print("Dados guardados com sucessos")