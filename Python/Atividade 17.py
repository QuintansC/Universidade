def calculaLitros(meters):
    return meters/6

def calculaMeters(litros):
    return litros*6

def calculaDiff(litros, qtdLatas):
    result = (litros - (qtdLatas*18)) / 3.6

    if (litros - (qtdLatas*18)) % 3.6 != 0:
        return int(result) + 1
    else:
        return result
    
try:
    entradaMetros = int(input("Quantos metros deseja pintar?: "))
    litros = calculaLitros(entradaMetros)
    print(litros)
    result = litros / 18 
    if(litros % 18 != 0):
        print(str(int(result + 1)) + ' Latas de Tinta no Valor de ' +str(int(result + 1) * 80))
    else:
        print(str(int(result)) + ' Latas de Tinta no Valor de ' +str(int(result) * 80))
    
    resultGalao = litros / 3.6

    if(litros % 3.6 != 0):
        print(str(int(resultGalao+2)) + ' Galões de tinta no Valor de ' + str(int(resultGalao+2) * 25))
    else:
        print(str(int(resultGalao)) + ' Galões de tinta no Valor de ' + str(int(resultGalao) * 25))
  

    print('\n \n')
    
    diffGaloes = calculaDiff(litros, int(result))
    print(
        str(int(result)) + 
        ' Latas de Tinta no Valor de ' +
        str(int(result) * 80)+ '\n e \n' + 
        str(diffGaloes) + 
        ' Galões de tinta no Valor de ' +
        str(str(diffGaloes * 25))
    )
except:
    print('Por favor digite um numero valido')
