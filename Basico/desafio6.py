nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

frequencia = int(input("Digite sua frequencia: "))

dispensa = input("Você possui dispensa da disciplina (S/N):")

if dispensa == "S" or dispensa == "s":
    esta_dispensado = True
else:
    esta_dispensado = False

media = (nota1 + nota2 + nota3) /3
media = round(media, 2)

if not esta_dispensado:
    if media >= 0 and media <= 100 and frequencia >= 75:

        if media >= 70:
            print("Aprovado")
        elif media >= 40 and media < 70:
            print("Exame")
        else:
            print("Reprovado")

        print("Sua media foi:", media)

    elif media >= 0 and media <= 100 and frequencia < 70:
        print("Reprovado, frequencia menor que 75%")
    else:
        print("Erro no valor da media, calcule novamente")
else:
    print("Voocê esta aprovado por dispensa")