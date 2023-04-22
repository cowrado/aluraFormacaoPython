print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto= 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}.".format(rodada,total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    elif(maior):
        print("Você errou. Seu chute foi maior que o número secreto.")
    else:
        print("Você errou. Seu chute foi menor que o número secreto.")

print("Fim de jogo")