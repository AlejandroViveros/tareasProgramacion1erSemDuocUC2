puntaje = 0
edad = int(input('ingrese su edad: '))
if (edad >= 18):
    print("Usted es mayor de edad")
else:
    print('es menor de edad')

login = input('Ingrese su nombre de usuario: ')
contra = input('Ingrese su contraseña: ')
if (login != "pedro" or contra != "1234") and (login != "angel" or contra != "a4s1"):
    print('Su usuario o contraseña son incorrectos')
else:
    print('Bienvenido al sistema')
    print("ahora debera ingresar 3 notas para poder calcular su promedio")
    nota1 = int(input('Ingrese nota numero 1: '))
    nota2 = int(input('Ingrese nota numero 2: '))
    nota3 = int(input('Ingrese nota numero 3: '))
    promedio = (nota1 + nota2 + nota3) / 3
    print('Su promedio es', promedio)

    if (promedio >= 4):
        print("Usted a aprobado!! ")
    else:
        print("Usted ha reprobado")

    pregunta1 = input(
        'Cual de los siguientes animales viven en el agua?\n 1)perro \n 2)cocodrilo \n 3)conejo \n 4)tiburon \n Escriba su respuesta :')
    if (pregunta1 == "cocodrilo"):
        puntaje = puntaje + 0.5
        print("El puntaje obtenido es: ", puntaje)
    elif (pregunta1 == "tiburon"):
        puntaje1 = puntaje + 1
        print("el puntaje obtenido es: ", puntaje1)
    else:
        print("Lamentablemente ese animal no vive en el agua, su puntaje es", puntaje)
        print("No se preocupe, quedan 3 preguntas")

    pregunta2 = input(
        "Cual es el equipo con mas copas en la liga chilena? \n 1)ñublense \n 2)cobreloa \n 3)colo-colo \n 4)cobresal \n Escriba su respuesta : ")
    if (pregunta2 == "colo-colo"):
        puntaje2 = puntaje1 + 1
        print("Correcto!, el puntaje total es de: ", puntaje2)
    else:
        puntaje2 = puntaje
        print("No obtuvo puntos esta vez, su puntaje es: ", puntaje2)

    pregunta3 = input(
        "Cual fue el nombre de la compañia que fundo steve jobs? \n 1)apple \n 2)windows \n 3)microsoft \n 4)office \n Escriba su respuesta : ")
    if (pregunta3 == "apple"):
        puntaje3 = puntaje2 + 1
        print("Correcto!, el puntaje total es de: ", puntaje3)
    else:
        puntaje3 = puntaje2 + 0
        print("No obtuvo puntos esta vez, su puntaje es: ", puntaje3)

    pregunta4 = input(
        "De que pelicula viene el personaje shrek? \n 1)bambie \n 2)shrek \n 3)pinocho \n 4)spiderman \n Escriba su respuesta : ")
    if (pregunta4 == "shrek"):
        puntaje4 = puntaje3 + 1
        print("Correcto!, el puntaje total es de: ", puntaje4)
    else:
        puntaje4 = puntaje3 + 0
        print("No obtuvo puntos esta vez, su puntaje es: ", puntaje3)









