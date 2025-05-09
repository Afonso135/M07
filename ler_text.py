"""
Programa para ler  e guardar  o que o utilizador escrever num ficheiro
Utilização:
    py ler_text-l[NOME_FICHEIRO] o program deve abrir o ficheiro indicado ou predefenido e mostrar todo o seu conteudo
    py ler_text-a[NOME_FICHEIRO] o program deve adicionar  ao ficheiro indicado tudo o que o utilizador escreve
"""
import sys  #para fornecer acesso aos parâmetros das linhas de comando
import os
#ler uma frase
NOME_FICHEIRO="poema.txt"
def Adicionar():
    texto=input(">_")
    with open(NOME_FICHEIRO,"a",encoding="utf-8") as f:
        while True:
            if texto=="":
                f.write(texto+"/n")
            else:
                break
def Ler():
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as f:
        if os.path.exists(NOME_FICHEIRO)==False:
            print("o ficheitro não existe")
        linhas=f.readlines
        for linha in linhas:
            print(linha)


    



def main():
   global NOME_FICHEIRO
   if len(sys.argv)<=1:
      print("Utilização:py ler_text-l[NOME_FICHEIRO]")
      return
   #ler o onme do ficheiro
   if len(sys.argv)==3:
      NOME_FICHEIRO=sys.argv[2]
    #opção
    op=sys.argv[1]
   if op=="a":
      Adicionar()
   if op.lower=="-l":
        Ler()
    if
        print("essa opção não existe")

if __name__=="main":
    main()