# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [ ] 1. O aluno deverá digitar 3 notas através do teclado
#   [ ] 2. Seu programa deverá calcular a média das notas    
#   [ ] 3. A partir da média, verificar qual situação o aluno se encontra 
# conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   [ ] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [ ] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de digitação
#   [ ] 6. Mostrar na tela para o aluno a situação final baseado na nota digitada.

Nota = int(input("Digite sua Nota: "))

if Nota < 0   or Nota > 100:
    print("Erro digitação!!")
else:
    if Nota > 70:
        print("Aprovado")
    elif Nota >= 40  and Nota <= 70:
        print("Você esta de exame!!")
    else:
        print("Reprovado")



