def validaDia(value: int, dias: []):
  if(value > 7):
    return 'Valor inválido'
  else:
    result = value -1
    return dias[result]

diaDaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
valueData = int(input('Qual dia da semana?: '))

print(validaDia(valueData, diaDaSemana))