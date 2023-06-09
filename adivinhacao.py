import random

print("***************************************")
print("** Bem vindo ao Jogo de Adivinhação! **")
print("***************************************")

numero_secreto = random.randint(1, 100)
total_de_tetnativa = 0
pontos = 1000

print("(1) Fácil (2) Moderado (3) Difícil")
nivel = int(input("Selecione a dificuldade: "))

if (nivel == 1):
    total_de_tetnativa = 15
elif (nivel == 2):
    total_de_tetnativa = 10
else:
    total_de_tetnativa = 5

for rodada in range(1, total_de_tetnativa + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tetnativa))

    chute = int(input("Digite um número entre 1 e 100: "))

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto

    if (acertou):
        print("Parabéns! Você acertou e fez {} pontos".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

print("Fim de Jogo!")
