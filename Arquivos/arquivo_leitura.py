# Leitura de arquivos -txt

def main():
    
    # Leitura de arquivo utilizando o r -  read
        
    arquivo = open("texto.txt", "r")

    if arquivo.mode == 'r': # verifica se o arquivo existe
        linhas = arquivo.readlines()
        
        # print(linhas)
        for 1 in linhas:
            print(1)



    arquivo.close()


if __name__ == "__main__":
    main()