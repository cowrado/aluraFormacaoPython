print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto= 42
total_de_tentativas = 3
rodadas = 1

while (rodadas <= total_de_tentativas):
    print("Tentativa {} de {}.".format(rodadas,total_de_tentativas))
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
        rodadas +=1
    else:
        print("Você errou. Seu chute foi menor que o número secreto.")
        rodadas +=1

print("Fim de jogo")