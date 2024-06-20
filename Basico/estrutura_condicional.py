# As estruturas de Decisão ou Condicionais em programação
# são utilizadas para tomar decisões com base em condições


# if

idade = int(input("Digite sua idade:"))
 



if idade >= 18 and idade < 60:
    print("Você é uma jovem")
elif idade >= 60:
    print("Você esta na melhor idade")
else:
    print("Você é menor de idade")

print("FIM")