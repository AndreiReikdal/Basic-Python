# forca.py
import random

def jogar(palavras = open("palavras.txt", "r")):

     imprime_mesagem_abertura()

     palavra_secreta = carrega_palavra_secreta()
     letras_acertadas = inicializa_letras_acertadas(palavras)


     enforcou = False
     acertou = False
     erros = 0
     print(letras_acertadas)

     while (not acertou and not enforcou):


          chute = input("Qual letra ?")
          chute: str = chute.strip()

          if (chute in palavra_secreta ):
               index = 0
               for letra in palavra_secreta :
                    if (chute == letra):
                         letras_acertadas[index] = letra
                    index = index + 1
          else :
               erros += 1
          enforcou = erros == 6
          acertou = "_" not in letras_acertadas
          print(letras_acertadas)

     if (acertou):
          print("Você ganhou!!")
     else:
          print("Você perdeu!!")
     print("fim de jogo")

def imprime_mesagem_abertura():
          print("*********************************")
          print("***Bem vindo ao jogo da Forca!***")
          print("*********************************")

def carrega_palavra_secreta():
          arquivo = open("palavras.txt", "r")
          palavras = []

          for linha in arquivo:
               linha = linha.strip()
               palavras.append(linha)

          arquivo.close()

          numero = random.randrange(0, len(palavras))
          palavra_secreta = palavras[numero].upper()

          return palavra_secreta

def inicializa_letras_acertadas(palavras):
          return ["_" for letra in palavras]



if (__name__ == "__main__"):
     jogar()