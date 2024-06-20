import carro
# do arquivo carro.py a classe Carro
from carro import Carro


def main():

    carro1 = Carro("Toyota","Etios")
    carro2 = Carro("VW","Up")    

    carro1.marca = "Toyota"
    carro1.modelo ="Etios"

    carro2.marca ="VW"
    carro2.modelo ="Up"

    carro1.imprimirDados()
    carro2.imprimirDados()

    print(f" O modelo do carro 1 é {carro1.modelo} é a marca é {carro1.marca}")
    

if __name__ == "__main__":
    main()