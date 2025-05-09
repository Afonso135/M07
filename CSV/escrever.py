lista=[
    {
        "nome":"afonso"
     "morada":"Viseu"
     "idade":30},

     {"nome":"alexandre"
     "morada":"amadora"
     "idade":38
    }
]

import csv #permite ler ou escrever em ficheiros de formato CSV
#cabecahlo do ficheiro 
chaves=lista[0].keys()
with open("ficheiro.csv","w",encoding="utf-8",newline="") as f:
#variável para guardar no ficheiro
    escrever=csv.DictWriter(f,fieldnames=chaves)
#gravar o cabecalho
escrever.writeheader
for i in range (len(lista)):
    escrever.writerow(lista[i]) #grava os dados correspondentes ao chaves do dicionário

print("ficheiro criado com sucesso")