import random

sorteio = random.randint(0, 10)
print(sorteio)
print(f"\033[1mSou seu computador...\nAcabei de pensar em número entre 0 a 10.\nSerá que você consegue adivinhar qual foi? ")

tentativa = 1 
palplite = int(input("\033[34m\nQual é seu palpite? "))

while palplite != sorteio:
  if palplite < sorteio:
   print("\033[35mMais...Tente novamente...")
  else:
    print("\033[31mMenos...Tente novamente...")
  palplite = int(input("Qual é seu palpite? "))
  tentativa += 1
print(f"\033[32mAcertou com {tentativa} tentativa. Parebéns") 
