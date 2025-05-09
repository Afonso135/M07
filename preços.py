"""
Program para criar um com produtos e preços
"""
NOME="preços.txt"
import os
if os.path(NOME)==False:
    print("Ainda não há produtos")

def ficheiro_existe():
    if os.path(NOME)==False:
        print("Ainda não há produtos")
        return False
    return True  

def Adicionar_produtos():
    with open("preços.txt","w",endcoding="utf-8")as f:
        nome=input("insira o nome do produto")
        preço=float(input("insira o preço do produto"))
        linha=f"{nome}-{preço}\n"
        f.write(linha)

def Ler_produto():
     with open(NOME,"r",endcoding="utf-8")as f:
         while True:
             linha=f.readline()
             if  not linha:
                break
             partes=linha.split("-")
             nome=partes[0].strip()
             preço=float(partes[1].strip())
             print("Produto:{nome} {preço}€")

def menu():
    op=0
    while op!=5:
        op=int(input())
        if op==1:
            Adicionar_produtos()
        if op==2:
            Ler_produto()
        if op==3:
            Editar()
        if op==4:
            Apagar()
            
def Editar():
    #verificar se existe o ficheiro
    if ficheiro_existe(NOME)==False:
        return
    #ler nome do produto a editar
    produto=input("insira o nome do produto a editar ")
    #abrir o ficheiro dos produtos a ler
    ficheiro_ler= open(NOME,"r",encoding="utf-8")
    #abrir o ficheiro tempporário para escrever
    ficheiro__escrever= open("temp.txt","w",endcoding="utf-8")
    #ler um produto
    while True:
        linha=ficheiro_ler.readline()
        if not linha:
            break
        #verificar se e o produto a editar
        partes=linha.split("")
        if NOME==partes[0].strip():
        #se sim gravar os novos dados
            novo_nome=input("insira um novo produto")
            novo_preço=float(input("insira um novo preço"))
            linha=f"{novo_nome}-{novo_preço}\n"
        #gravar no ficheiro temporário
        ficheiro__escrever.write(linha)
    #fechar os ficheiro
    ficheiro__escrever.close()
    ficheiro_ler.close()
    #apagar o ficheiro dos produtos
    os.remove(NOME)
    #mudar o onme do ficheiro
    os.rename("temp.text",NOME)
    print("produto alterado com sucesso")

def Apagar():
    #verificar se existe o ficheiro
    if ficheiro_existe(NOME)==False:
        return
    #ler nome do produto a editar
    produto=input("insira o nome do produto a editar ")
    #abrir o ficheiro dos produtos a ler
    ficheiro_ler= open(NOME,"r",encoding="utf-8")
    #abrir o ficheiro tempporário para escrever
    ficheiro__escrever= open("temp.txt","w",endcoding="utf-8")
    #ler um produto
    while True:
        linha=ficheiro_ler.readline()
        if not linha:
            break
        #verificar se e o produto a apagar
        partes=linha.split("")
        if NOME==partes[0].strip():
        #se sim gravar os novos dados
           continue
        #gravar no ficheiro temporário
        ficheiro__escrever.write(linha)
    #fechar os ficheiro
    ficheiro__escrever.close()
    ficheiro_ler.close()
    #apagar o ficheiro dos produtos
    os.remove(NOME)
    #mudar o onme do ficheiro
    os.rename("temp.text",NOME)
    print("produto apagado com sucesso")
    
Adicionar_produtos()



