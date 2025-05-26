"""
Programa para gravar um nº inteiro num ficheiro binário
"""
import struct

n=1234

#gravar o nº no ficheiro int.dat
with open("int.dat","wb") as f:
    #empacotar o nº no formato inteiro e escrever no ficheiro
    f.write(struct.pack("i",n))
print("Número gravado com sucesso")
