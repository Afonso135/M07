"""
Ler um nº inteiro de um ficheiro binário
"""
import struct

with open("int.dat","rb") as f:
    n=struct.unpack("i",f.read(4))
print(n[0])