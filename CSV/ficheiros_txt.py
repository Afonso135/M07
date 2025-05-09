#Ficheiros de Texto

"""Existem 3 maneiras de abrir um ficheiro:
    w-escrever e se o ficheiro não existir cria o  mesmo
    r-para leitura
    a-para acrescentar algo ao ficheiro(destruíndo o original)
"""

"""abrir o ficheiro"""

#ficheiro=open("nome do ficheiro.txt","a maneira de abretura",encoding="utf-8")
                    #ou
#with open("nome do ficheiro.txt","a maneira de abretura",encoding="utf-8")
    #da segunda forma não e´necessário fechar o ficheiro

"""fechar o ficheiro"""
#ficheiro.close()    só seve se abrir da 1ª maneira

#ler o  ficheiro(r)-usar função readlines()
#escrever(w)-uasr função write() 