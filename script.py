nomes_arquivos = ["ex7.py", "ex8.py ", "ex9.py", "ex10.py", "ex11.py", "ex12.py","ex13.py"]


for nome_arquivo in nomes_arquivos:
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"o `{nome_arquivo}` criado com sucesso!")

    print(f"o `{nome_arquivo}` criado com sucesso!")