def trataNumbers(numberFirst: int, numberSecond: int, numberThird: int):
  if(numberFirst > numberSecond and numberFirst > numberThird):
    if(numberSecond < numberThird):
      return [numberFirst, numberSecond]
    else:
      return [numberFirst, numberThird]
  else:
    if(numberSecond > numberFirst and numberSecond > numberThird):
      if(numberThird<numberFirst):
        return [numberSecond, numberThird]
      else:
        return [numberSecond, numberFirst]
    else:
      if(numberSecond < numberFirst):
        return [numberThird, numberSecond]
      else: 
        return [numberThird, numberFirst]

entradaPrimeiroValor = int(input("Primeiro valor de entrada?: "))
entradaSegundoValor = int(input("Segundo valor de entrada?: "))
entradaTerceiroValor = int(input("Terceiro valor de entrada?: "))

result = trataNumbers(entradaPrimeiroValor, entradaSegundoValor, entradaTerceiroValor)

print("\n O maior valor é: " + str(result[0]) +" \n O menor valor é: "+ str(result[1]))