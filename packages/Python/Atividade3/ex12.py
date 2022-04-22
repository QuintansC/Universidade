def trataImpostoDeRenda(salario: float):
  if(salario < 900.00):
    return [0, ' 0%']
  else:
    if(salario > 900.00 and salario < 1500.00):
      return [salario * 0.05, ' 5%']
    else:
      if(salario > 1500.00 and salario < 2500.00):
        return [salario * 0.10, '10%']
      else:
        return [salario * 0.20, '20%']

horas = float(input('Qual é o carga horária mensal?: '))
precoHoras = float(input('Qual é o valor por hora?: '))

salarioBruto = horas * precoHoras

ir = trataImpostoDeRenda(salarioBruto)
inss = salarioBruto*0.10
fgts = salarioBruto*0.11
sindicato = salarioBruto*0.03

somaDescontos = ir[0] + inss + sindicato
salarioLiquido = salarioBruto - somaDescontos

print(
  "\n O salário Bruto é:       R$"+ str(salarioBruto)+
  "\n (-) IR ("+ir[1]+"):            R$"+ str(ir[0])+
  "\n (-) INSS (10%):          R$"+ str(inss)+
  "\n FGTS (11%):              R$"+ str(fgts) + 
  "\n Sindicato (3%):          R$"+ str(sindicato) + "\n"+
  "\n Total de Descontos:      R$"+ str(somaDescontos)+
  "\n Salário Líquido:         R$"+ str(salarioLiquido)
)
