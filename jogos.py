import niveis
import forca

print("**********************************")
print("****** Escolha o seu jogo! *******")
print("**********************************")

print("** (1) Adivinhação ou (2) forca **")

jogo = int(input("Qual jogo?: "))

if jogo == 1:
    print("*** Jogando adivinhação ***")
    niveis.jogar()
elif jogo == 2:
    print("*** Jogando Forca ***")
    forca.jogar()