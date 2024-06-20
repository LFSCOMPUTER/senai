#Descobrir se o triangulo é
#   Equilátero ( todos lados iguais)
#   Isoceles (2 lados iguais)
#   Escaleno (todos os lados diferentes)

l1 = int(input("Digite um lado l1 do triangulo: "))
l2 = int(input("Digite um lado l2 do triangulo: "))
l3 = int(input("Digite um lado l3 do triangulo: "))


if l1 ==l2 and l2 == l3 and l1 == l3:
    print("Equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Isoceles")
else:
    print("Escaleno")

