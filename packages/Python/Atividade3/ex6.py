def trataNumbers(numberFirst: int, numberSecond: int, numberThird: int):
  if(numberFirst > numberSecond and numberFirst > numberThird):
    return numberFirst
  else:
    if(numberSecond > numberFirst and numberSecond > numberThird):
      return numberSecond
    else:
      return numberThird

entradaPrimeiroValor = int(input("Primeiro valor de entrada?: "))
entradaSegundoValor = int(input("Segundo valor de entrada?: "))
entradaTerceiroValor = int(input("Terceiro valor de entrada?: "))

result = trataNumbers(entradaPrimeiroValor, entradaSegundoValor, entradaTerceiroValor)

print(result)