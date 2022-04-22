def calculaMedia(nota1: int, nota2: int):
  media = (nota1+nota2)/2 
  return media

def avaliacao(nota: int):
  if(nota == 10):
    return 'Aprovado com Distinção'
  elif(nota >= 7):
    return 'Aprovado'
  else:
    return 'Reprovado'

nota1 = int(input("Primeira nota?: "))
nota2 = int(input("Segunda nota?: "))

result = calculaMedia(nota1, nota2)
result = avaliacao(result)
print(result)