with open("alunos.txt","r"endcoding="utf-8") as f:
    Texto=f.readline()
    print(Texto)
    f.seek()
    Texto=f.readline()
    print(Texto) 