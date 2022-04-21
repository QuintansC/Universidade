def trataNumbers(numberFirst: int, numberSecond):
  if(numberFirst > numberSecond):
    return numberFirst
  else:
    if(numberFirst == numberSecond):
      return 'Os numeros são iguais'
    else:
      return numberSecond

entradaPrimeiroValor = int(input("Primeiro valor de entrada?: "))
entradaSegundoValor = int(input("Segundo valor de entrada?: "))

result = trataNumbers(entradaPrimeiroValor, entradaSegundoValor)

print(result)