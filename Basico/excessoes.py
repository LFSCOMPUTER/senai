# def main():
#     try:

#         valor = int(input("Digite um numero:"))
#         resultado = 100 / valor
#     except ZeroDivisionError:
#         print("Erro: Divisao por zero!!")
#     except ValueError:
#         print("Erro: valor inserido não é um numero valido!!")
#     else:
#         print("Resultado:", resultado)


#     print("Resultado:", resultado)
try:
    valor = int(input("Digite um numero:"))
    resultado = 100 / valor
except Exception as e:
    print(f"Erro: {type(e).__name__}: (e)")
else:
    print("Resultado:", resultado)



if __name__ == "__main__":
    main()