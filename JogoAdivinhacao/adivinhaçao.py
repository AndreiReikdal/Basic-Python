# AULA 1
import random
def jogar():
     print("*********************************")
     print("Bem vindo ao jogo de Adivinhação!")
     print("*********************************")

     numero_comando = random.randrange(1, 100)
     tentativas = 0
     pontos = 100

     print("Qual o nível de dificuldade?")
     print("(1) Fácil (2) Médio (3) Difícil")

     nivel = int(input("Defina o nível: "))

     if (nivel == 1):
         tentativas = 20
     elif (nivel == 2):
         tentativas = 10
     else:
         tentativas = 5

     for rodada in range(1, tentativas + 1):
         print("Tentativa {} de {}".format(rodada, tentativas))
         chute_str = input("Digite um número entre 1 e 100: ")
         print("Você digitou: ", chute_str)
         chute = int(chute_str)

         if (chute < 1 or chute > 100):
             print("Você deve digitar um número entre 1 e 100!")
             continue

         acertou = numero_comando == chute
         maior = chute > numero_comando
         menor = chute < numero_comando

         if (acertou):
             print("Você acertou e fez {} pontos!".format(pontos))
             break
         else:
             if (maior):
                 print("Você errou! O seu chute foi maior que o número secreto.")
             elif (menor):
                 print("Você errou! O seu chute foi menor que o número secreto.")
             pontos_perdidos = abs(numero_comando - chute)
             pontos = pontos - pontos_perdidos

     print("Fim do jogo")
if (__name__ == "__main__"):
    jogar()