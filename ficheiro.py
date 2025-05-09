#Ficheiros
"""
1-Abrir ficheiro
    ficheiro=open("nome.extensão)
2-Ler /Escrever
3-Fechar
    ficheiro.close()
"""
ficheiro=open("alunos.txt","r",encoding="utf-8")
ficheiro.write("ola mundo")
ficheiro.write("fim")
ficheiro.close()