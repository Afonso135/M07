"""program para gerar desculpas"""
import random
import os

NOME1="intro.txt"
NOME2="culpado.txt"
NOME3="desculpa.txt"

def intro(lista):
    """Função que devolve uma linha aleatória"""
    if os.path.exists((NOME1))==False:
        print("fivheiro não existe")
        with open("intro.txt") as f:
            f.readlines()
            random.choise(lista)


def desculpa(lista):
    if os.path.exists((NOME2))==False:
        with open("desculpa.txt") as f:
            f.readlines()
            random.choise(lista)

        


def culpado(lista):
    if os.path.exists((NOME3))==False:
        with open("culpado.txt") as f:
            f.readlines()
            random.choise(lista)
