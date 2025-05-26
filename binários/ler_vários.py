"""
programa para ler dados de um ficheiro binário
"""
import struct

with open("dados.bin",'rb')as f:
    #ler os dados
    dados_bin=f.read(28)
    dados_bin=struct.unpack("20sif",dados_bin)

#converter a str binária numa str
nome=dados_bin[0].decode("utf-8").rstrip("\x00")

print("Nome: ",nome)
print("Idade: ",dados_bin[1])
print("Saldo: ",dados_bin[2])