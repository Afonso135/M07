"""
programa para ler e guardar dados num ficheiro csv
para carros e pilotos de corrida
carros.csv:marca,modelo,matricula
pliotos.csv:nome, idade,pais

Funcionalidades:
    Adicionar:carros,pilotos
    Listar:carros,pilotos
    Pesquisar:Pilotos de um carro,carro de um piloto
"""

import csv
import os

def menu(): 
    global lista_carros,Lista_pilotos
    lista_carros=Ler(NOME)
    Lista_pilotos=Ler(NOME2)
    op=0
    while op!=4:
        op=int(input("1.Adicionar\n2.Lstar\n3.Pesquisar\n.4Sair,insira uma opção:"))
        if op==4:
            break    
        if op==1:
            Adicionar()
        if op==2:
            Listar()
        if op==3:
            Pesquisar()

lista_carros=[]
Lista_pilotos=[]

  
NOME="carros.csv"
NOME2="pilotos.csv"

def validar_NRmatricula(matricula):
    """Devolve o nº de pilotos nuum carro"""
    for p in Lista_pilotos:
        if p["matricula"]==matricula:
            contar=contar+1    

def Adicionar():
    ad=input("insira o que quer p/c:")
    if not ad:
        return
    if ad=="c":
        #ler dados do carro
        marca=input("insira a marca do carro:")
        #verifiacr se a matru«icula existe
        modelo=input("insira o modelo do carro:")
        matricula=input("insira a matricula do carro:")
        #validar a matricula
        if validar_matricula==True:
            print("a matricula já existe")
            #verificar se o carro está cheio
        if validar_NRmatricula(matricula)>=2:
            print("já existem dois pilotos")
        #criar um dicionário
        novo_carro={"marca":marca,"modelo":modelo,"matricula":matricula}
        #adicionar á lista
        lista_carros.append(novo_carro)
        #escrever nos ficheiro dos carros
        Escrever(lista_carros,NOME)
    if ad=="p":
        #ler daos do piloto
        nome=input("insira o o nome do piloto:")
        idade=input("insira a sua idade:")
        país=input("insira o seu pais:")
        #validar matricula
        if validar_matricula==True:
            print("a matricula já existe")
        #criar um dicionário
        novo_piloto={"nome":nome,"idade":idade,"pais":país}
         #adicionar á lista
        Lista_pilotos.append(novo_piloto)
        print("pilot adicionado com sucesso")
        #escrever nos ficheiro dos pilotos

def validar_matricula(matricula): 
    """Função para verificar se a matricula inserida existe"""
    for carro in lista_carros:
        if "matricula"[carro]==matricula:
            return True
        return False


def Listar():
    op=input("insira o que quer p/c:")
    if op=="c":
        print(lista_carros)
    if op=="p":
        print(Lista_pilotos)

def Pesquisar(piloto):
    matr=input("insira uma matricula a pesquisar")
    if matr:
        #mostrar pilotos do carro
        for piloto in lista_carros:
            if piloto["matricula"]==piloto:
                print(piloto)
        piloto=input("qual o nome do piloto")
        if piloto:
            #mostrar o carro do piloto
            for p in Lista_pilotos:
                if p["nome"]==piloto:
                    for c in lista_carros:
                        if p["matricula"]==c["matricula"]:
                            print(c)



    

def Escrever(lista,chaves,NOME):
    with open("NOME.csv","w",encoding="utf-8",newline="") as f:
#variável para guardar no ficheiro
        escrever=csv.DictWriter(f,fieldnames=chaves)
#gravar o cabecalho
    escrever.writeheader
    for i in range (len(lista)):
        escrever.writerow(lista[i]) #grava os dados correspondentes ao chaves do dicionário

def Ler(NOME):
    #listta vazia para guardar os dados do ficheiro
    dados=[]
#verificar se o ficheiro existe
    if os.path.exists(NOME)==False:
        return dados
#abrir o ficheiro
    with open("NOME","r",encoding="utf-8") as f:
    #criar o objeto para ler o ficheiro
        ler=csv.DictReader(f)

    #ler cada linha do ficheiro
    for linha in ler:
        dados.append(linha)
    return dados

if __name__=='__main__':
    menu()