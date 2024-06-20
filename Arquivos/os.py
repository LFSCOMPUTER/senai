#OS -Operating System ou Sistemas Operacionais
#Pastas (Diretorios)
#Locais  ( caminhos/Path)

import os

def main():

    diretorio = "C:\\temp"Python313"

    arquivos = os.listdir(diretorio)

    for arq in arquivos:
        print(arq)

        


    data_hoje = str(date.today())
    nova_pasta = "C/Temp/" + data_hoje



    # Cria uma nova pasta/diretorio
    os.makedirs(nova_pasta)






if __name__ == "__main__":
    main()


