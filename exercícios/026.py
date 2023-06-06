frase = str(input("Digite uma frase: ")).strip().lower()
letra = str(input("escolha uma letra para ser verificada: ")).strip().lower()
print('')
print(
  f"Analisando a frase...\n\nA letra {letra} apareceu {frase.count(letra)} vezes\nA posição em que ela apareceu pela a primeira foi {frase.find(letra)}\nA ultima letra {letra} aparece na posição {frase.rfind(letra)}"
)