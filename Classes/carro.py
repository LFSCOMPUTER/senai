class Carro:
    #caracteristicas
    ano = 0
    marca = ""
    modelo = ""

    # Metodo Construtor: executado automaticamente quando pbjeto é criado
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 
        

    # Funcionalidades (funções => metodos)
    def imprimirDados(self):
        print(f"A marca do meu carro eh {self.marca} e o modelo eh {self.modelo}")
  
 