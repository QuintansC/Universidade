def trataLetters(parameter: str):
  parameter = parameter.lower()
  if(parameter == 'f'):
    return 'Feminino'
  else:
    if(parameter != 'f' and parameter != 'm') :
      return 'Sexo inválido'
    else:
      return 'Masculino'
print("F - Feminino / M - Masculino")
character = str(input("Qual seu Sexo?: "))
result = trataLetters(character)

print(result)