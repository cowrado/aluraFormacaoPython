def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, index))
            index += 1

        print("Jogando...")

if (__name__ == "__main__"):
    jogar()