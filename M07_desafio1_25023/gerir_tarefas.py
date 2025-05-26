"""Programa para gerir tarefas com ficheiro de texto"""

import csv
import os
import datetime

tarefas=[]
NOME="tarefas.txt"

def menu(): 
    op=0
    while op!=5:
        op=int(input("1.Adicionar tarefa\n2.Listar tarefas\n3.Remover tarefa\n4.Marcar tarefa como concluída\n5.Sair\ninsira uma opção:"))
        if op==5:
            break    
        if op==1:
            Adicionar()
        if op==2:
            Listar()
        if op==3:
            Remover()
        if op==4:
            Concluir()

def Adicionar():
        
        with open(NOME,"a",encoding="utf-8") as t:
            descrição=input("insira uma breve descrição da tarefa:")
            data=input("insira a data da tarefa:")
            nova_tarefa=f"descrição:{descrição},data:{data}\n" 
            t.write(nova_tarefa)
            print("tarefa adicionada com sucesso")

def Listar():
     if os.path.exists(NOME)==False:
        print("O ficheiro aind não  existe")
     with open(NOME,"r",encoding="utf-8") as t:
        tarefas=t.readlines()
        print(tarefas)


def Remover():
    if os.path.exists(NOME)==False:
        print("O ficheiro aind não  existe")
    else:
        with open(NOME,"a",encoding="utf-8") as t:
            tarefa=(input("insira a descrição da  tarefa a remover:"))
            if tarefa:
                for r in tarefas:
                    tarefa_remov=tarefas.remove(tarefa)
                    tarefas=t.write(tarefa_remov)
                    print("tarefa removida com sucesso")
        
    
    
def Concluir():
    if os.path.exists(NOME)==False:
        print("O ficheiro aind não  existe")
    else:    
        with open(NOME,"a",encoding="utf-8")as t:
            concluir=input("insira a descrição da tarefa:")
            for i in tarefas:
                if concluir:
                    t.write(f"[Concluída]{tarefas[i]}")
            print("A tarefa foi concluída")



if __name__=="__main__":
    menu()