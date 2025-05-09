with open("pessoas.txt","r",endcoding="utf-8")as ficheiro:
    while True:
        linha=ficheiro.readline()
        #verificar se encontrou o fim do ficheiro(enf of file)
        if not linha:
            break
        print(linha,end="")