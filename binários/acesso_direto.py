"""
Program par ler os dados de um registo com base no nº do registo 
"""

import os
import struct

TAMANHO_F=28

#calcular o tamanho do ficheiro
tamanho_f=os.path.getsize("dados.bin")
#calcular o nr de registos
n_registo=tamanho_f/TAMANHO_F

n_ler=int(input(f"tem{n_registo} qual o que pretende ler"))

if n_ler>n_registo:
    print("Não existe esse registo")
else:  
#abrir o ficheiro para leitura em modo binário
    with open("dados.bin","rb") as f:
        #posicionar o cursor no byte correspondente
        byte_ler=(n_ler-1)*TAMANHO_F
        f.seek(byte_ler)
        #ler os dados
        dados_bin=f.read(28)
        dados_bin=struct.unpack("20sif",dados_bin)
        #converter a str binária numa str
        dados=struct.unpack("20sif",dados_bin)
        print(dados[0].decode("utf-8")).rstrip("\x00")
        print(dados[1])
        print(dados[2])