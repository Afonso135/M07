import csv

#listta vazia para guardar os dados do ficheiro
dados=[]

#abrir o ficheiro
with open("ficheiro.csv","r",encoding="utf-8") as f:
    #criar o objeto para ler o ficheiro
    ler=csv.DictReader(f)

    #ler cada linha do ficheiro
    for linha in ler:
        dados.append(linha)