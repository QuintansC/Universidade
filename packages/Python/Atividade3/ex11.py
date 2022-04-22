def calculaDesconto(salario: float):
  if(salario < 280.00):
    return [salario * 0.20, '20%']
  else:
    if(salario > 280.00 and salario < 700.00):
      return [salario * 0.15, '15%']
    else:
      if(salario > 700.00 and salario < 1500.00):
        return [salario * 0.10, '10%']
      else:
        return [salario * 0.05, '5%']
        
salarioAtual = float(input('Qual é o salário?: '))
arrayDeReajustes = calculaDesconto(salarioAtual)
salarioComReajuste = salarioAtual + arrayDeReajustes[0]
print(
  "\n O antigo salário é: "+ str(salarioAtual)+
  "\n O valor do Reajuste foi de: "+ str(arrayDeReajustes[0])+
  "\n O Reajuste foi de: "+ str(arrayDeReajustes[1])+
  "\n O novo salário é: "+ str(salarioComReajuste) + "\n"
)
