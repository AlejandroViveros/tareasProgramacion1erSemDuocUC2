valorTotal = 0
clienteP = ()
print('-----------------------------------------')
print('Bienvenido al sistemas de compras Duoc UC')
print('-----------------------------------------')
print('A continuacion debera elegir los productos \n que desea comprar, indicando "si" o "no" ')
print("------------------------------------------")
print ('Lista de productos y precios \n 1)agua-$600 \n 2)azucar-$1200 \n 3)aceite-$1500 \n 4)arroz-$1250 \n 5)fideos-$790 \n 6)bebida-$1780 \n 7)chocolate-$2500 \n 8)Pan de Molde-$1340 ')
print("------------------------------------------")
agua = input('Desea llevar agua?: ')
azucar = input('Desea llevar azucar? :')
aceite = input('Desea llevar aceite?')
arroz = input('Desea llevar arroz? :')
fideos = input('Desea llevar fideos? :')
bebida = input('Desea llevar bebida?: ')
chocolate = input('Desea llevar chocolate?: ')
panMolde = input('Desea llevar pan de molde? :')

if (agua == "si"):
    valorTotal1 = valorTotal + 600
elif(agua == "no"):
    valorTotal1 = valorTotal + 0

if (azucar == "si"):
    valorTotal2 = valorTotal1 + 1200
elif(azucar == "no"):
    valorTotal2 = valorTotal1 + 0

if (aceite == "si"):
    valorTotal3 = valorTotal2 + 1500
elif(aceite == "no"):
    valorTotal3 = valorTotal2 + 0

if (arroz == "si"):
    valorTotal4 = valorTotal3 + 1250
elif(arroz == "no"):
    valorTotal4 = valorTotal3 + 0

if (fideos == "si"):
    valorTotal5 = valorTotal4 + 790
elif(fideos == "no"):
    valorTotal5 = valorTotal4 + 0

if (bebida == "si"):
    valorTotal6 = valorTotal5 + 1780
elif(bebida == "no"):
    valorTotal6 = valorTotal5 + 0

if (chocolate == "si"):
    valorTotal7 = valorTotal6 + 2500
elif(chocolate == "no"):
    valorTotal7 = valorTotal6 + 0

if (panMolde == "si"):
    valorTotal8 = valorTotal7 + 1340
elif(panMolde == "no"):
    valorTotal8 = valorTotal7 + 0

print('Su total es de: ',valorTotal8)
print('-----------------------------------------')
preguntaCliente = input('usted es cliente preferencial? (indique "si" o "no"): ')

if (preguntaCliente == "si"):
    clienteP = True
    valorTotalDesc = valorTotal8*0.25
    valortotal9 = valorTotal8-valorTotalDesc
    print('Usted es un cliente preferencial por lo que recibe \n un descuento del 25% en el total de su compra \n su total es: ', valortotal9)
else:
    clienteP = False
    print('Usted no es cliente preferencial, su total es: ', valorTotal8)









