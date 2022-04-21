def trataNumbers(parameter: int):
  if(parameter > 0):
    return 'Esse numero é positivo'
  else:
    if(parameter == 0):
      return 'Esse numero é zero'
    else:
      return 'Esse numero é negativo'

value = int(input("Insira aqui o valor que deseja saber seu sinal: "))
result = trataNumbers(value)

print(result)