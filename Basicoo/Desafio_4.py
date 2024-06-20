# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escolar
#   1. O aluno deverá digitar sua nota através do teclado
#   2. Verificar qual situação o aluno se encontra conforme notas abaixo:
#       2.1 nota > 70 - aprovado
#       2.2 nota < 40 - reprovado
#       2.3 nota entre 40 e 70 - exame/recuperação
#   3. Mostrar na tela para o aluno a situação final baseado na nota digitada.

# IF / ELIF / ELSE

Nota = int(input("Digite sua Nota: "))

if Nota > 70:
    print("Aprovado")
elif Nota >= 40  and Nota <= 70:
    print("Você esta de exame!!")
else:
    print("Reprovado")