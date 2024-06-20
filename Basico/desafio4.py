# Desenvolver um programa para verificar a situação do aluno
# em relação a sua promoção escola
# 1. O aluno deverá digitar sua nota através do teclado
# 2. Verificar qual situação o aluno se encontra conforme notas abaixo:
#    2.1 nota > 70 - aprovado
#    2.2 nota < 40 - reprovado
#    2.3 nota entre e 70 - exame/recuperação
#3. Mostrar na tela para o aluno a situação final baseado na nota digitada

nota = int(input("Digite sua nota:"))
if nota >=40 and nota < 70:
    print("Você está recuperação")
elif nota < 40:
    print("Você esta reprovado")
else:
    print("Você esta aprovado")
