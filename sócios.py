NOME="acdamécio.txt"
NOME2="tondela.txt"

import os
#verificar se existem
if os.path(NOME)==False or os.path(NOME2)==False:
    print("Ainda não há sócios")
ficheiro=open("académico","w",encoding="utf-8")
socios_académico=ficheiro.readlines()
ficheiro2=open("tondela","w",endcoding="utf-8")
socios_tondela=ficheiro2.readlines()

for socio in socios_académico:
    if socio in socios_tondela:
        print(f"{socio} é sócio dos dois clubes")
encontra=True
if encontra==False:
    print("não existem traidores")


ficheiro.close()
ficheiro2.close() 
