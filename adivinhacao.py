print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou ", chute)

if numero_secreto == chute:
    print("Você acertou!")
else:
    if chute > numero_secreto:
        print("Você errou! Seu chute foi maior que o número secreto.")
    elif chute < numero_secreto:
        print("Você errou! Seu chute foi menor que o número secreto.")

print("******Fim de jogo.********")
