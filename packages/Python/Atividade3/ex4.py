def continus(parameter: bool):
  continuar =  input('Deseja continuar?')
  continuar = continuar.lower()
  if(continuar == 's' or continuar == 'y' or continuar == 'sim' or continuar == 'yes'):
    parameter == False
  else:
    exit()

vogais = ['a', 'e', 'i', 'o', 'u']
exits = False
while (exits == False):
  letter =  input('Digite aqui a Letra: ')
  for vogal in vogais:
    if(letter == vogal):
      print("A Letra é uma vogal \n")
      break
    else:
      print("A Letra é uma consoante \n")
      break
  continus(exits)
