print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")


numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print(f"Tentativa {rodada} de {total_de_tentativas}.")

    chute = int(input("Digite número entre 1 e 100: "))
    
    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! Seu chute foi menor que o número secreto.")
    rodada = rodada + 1

print("******Fim de jogo.********")
