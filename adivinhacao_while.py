import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("*********************************")

    #numero_secreto = round(random.random() * 100) # 0.0 até 1.0, portanto pode arredondar algo para zero
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Escolha o nivel: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while (rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        
        chute_str = input("Digite  um numero entre 1 e 100: ")
        print("Voce digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce DEVE digitar um numero entre 1 e 100 !")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Voce errou! O seu chute foi MAIOR que o numero secreto.")
                if (rodada == total_de_tentativas):
                    print("O numero secreto era {}. Voce fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Voce errou! O seu chute foi MENOR que o numero secreto.")
                if (rodada == total_de_tentativas):
                    print("O numero secreto era {}. Voce fez {}".format(numero_secreto, pontos))

        rodada = rodada + 1

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()