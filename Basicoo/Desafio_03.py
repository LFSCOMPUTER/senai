# Desafio 03
# Desenvolver um programa para uma loja de lanches (MAC)
# Requisitos:
# - O usuário vai receber uma mensagem de boas vindas
# - O sistema irá pedir qual seria a opção de lanche (Nº1, ...)
# - O sistema irá retornar o nome lanche e o valor dele
# - Usar pelo menos 4 opções de lanches
# - Usar pelo menos 4 opções de bebida

# - Para resolver usar listas  
print(f"Olá,Seja bem vindo MC!!")

lanches = ["Big Mac{$5,00}", "Quarteirao {$6,00}", "Mc Cheddar {$5,50}","XBURGUE {$7,00}"]
bebida = ["Heineken{$15,00}", "Antarctica{$11,00}", "Original {$13,50}","Spaten {$7,00}"]
Batata = ["Pequena{$5,00}", "Media{$11,00}", "Grande {$13,50}"]

opcao = int(input("Qual é sua opcao de lanche? "))

opcao = int(input("Qual é sua opcao de bebida? "))

opcao = int(input("Qual é sua opcao de Batata? "))

print("Voce escolheu o ", lanches[opcao-1])
print("Voce escolheu o ", bebida[opcao-1])
print("Voce escolheu o ", Batata[opcao-1])

