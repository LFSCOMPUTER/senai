# As maçãs custam R$0.30 cada se forem compradas menos
#do que uma duzia, e R$ 0.25 se forem compradas
#pelo menos doze. Escreva um programa que leia
#o número de maçãs compradas, calcule e escreva o valor
# total da compra


print("-------MAÇAS-----")

qtde_macas = int(input("Quantas maças deseja comprar?"))

if qtde_macas >= 12:
    print("O valor da sua compra é", (qtde_macas * 0.25))
else:
    print("O valor da sua compra é", (qtde_macas * 0.30))
