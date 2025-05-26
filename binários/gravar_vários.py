"""
Guardar num ficheiro binário os dados de um cliente :nome , idade e
saldo
"""
import struct
#ler dados
nome=input("insira um  nome: ")
idade=int(input("insira a sua idade: "))
saldo=float(input("Qual o saldo: "))

#adicionar ao ficheiro(dadosbin)
with open("dados.bin","ab") as f:
    #nome->str->cada letra um byte
    dados_pac=struct.pack("20s",nome.encode("utf-8"))
    f.write(dados_pac)
    # int->idade->4 bytes
    dados_pac=struct.pack("i",idade)
    f.write(dados_pac)
    # saldo->float->4 bytes
    dados_pac=struct.pack("f",saldo)
    f.write(dados_pac)
print("Dados guardados com sucesso")