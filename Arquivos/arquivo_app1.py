# Escrita de arquivos
def main():

    pessoas = [" Ana", "Joao","Bia","Jose"]
    salarios = [5000, 2300, 6200 , 9000]

    arquivo = open('texto.txt','w+')

    # Arquivo texto
    for i in range(4):
            arquivo.write('Nome:')
            arquivo.write('pessoas[i]:')
            arquivo.write('\tSalario:')
            arquivo.write(str(salarios[i]))
            arquivo.write('\n:')


    arquivo.close()

    if __name__ == "__main__":
        main()