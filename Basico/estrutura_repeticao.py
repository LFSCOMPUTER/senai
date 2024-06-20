#Estruturas de Repetição

frutas = ["pera", "maça", "banana", "laranja", "abacate", "abacaxi", "limão", "Melancia"]

# Estrutura de repetição FOR
# Melhor forma de se usar
#for f in frutas:
 #   print(f)

#for i in range(5):
 #   print(i)

#for i in range( len(frutas) ):
#    print(frutas[i])

#for x in range(5, 10):
#    print(x)

# Estrutura de Repetição WHILE

contador = 0

#while contador < 22:
   # print(contador)
    #contador += 1

nota = int(input("Digite a sua nota:"))

while nota < 0 or nota > 100:
    print("Sua nota deve estar entre 0 e 100, digite novamente")
    nota = int(input("Digite sua nota:"))