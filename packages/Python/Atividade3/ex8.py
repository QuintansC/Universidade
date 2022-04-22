def trataNumbers(priceFirst: int, priceSecond: int, priceThird: int):
  if(priceFirst > priceSecond and priceFirst > priceThird):
    if(priceSecond < priceThird):
      return [priceFirst, priceSecond]
    else:
      return [priceFirst, priceThird]
  else:
    if(priceSecond > priceFirst and priceSecond > priceThird):
      if(priceThird<priceFirst):
        return [priceSecond, priceThird]
      else:
        return [priceSecond, priceFirst]
    else:
      if(priceSecond < priceFirst):
        return [priceThird, priceSecond]
      else: 
        return [priceThird, priceFirst]

entradaProd1 = float(input("Valor do Primeiro Produto?: "))
entradaProd2 = float(input("Valor do Segundo produto?: "))
entradaProd3 = float(input("Valor do Terceiro de entrada?: "))

result = trataNumbers(entradaProd1, entradaProd2, entradaProd3)

print("O produto mais barato custa: "+ str(result[1]))