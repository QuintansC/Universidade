def trataTxt(text: str):
  newChar = text.lower()
  if(newChar == "m"):
    return 'Bom dia!'
  elif(newChar == "n"):
    return 'Boa noite!'
  elif(newChar == "v"):
    return 'Boa tarde!'
  else:
    return 'Valor inválido!'

print('Turnos: \n M - Matutino / V - Vespertino / N - Noturno')
result = str(input('Qual turno você estuda?: '))

result = trataTxt(result)
print(result)