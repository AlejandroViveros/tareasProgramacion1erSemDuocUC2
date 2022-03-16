edad = int(input('ingrese su edad: '))
sexo = input('ingrese su sexo: ')
if (edad >= 18):
    print("Usted es mayor de edad")
else:
    print('es menor de edad')
user1 = "pedro"
user2 = "angel"
contra1 = "1234"
contra2 = "a4s1"

login = input('Ingrese su nombre de usuario: ')
contra = input('Ingrese su contraseña: ')
if (login != "pedro" or contra != "1234") and (login != "angel" or contra != "a4s1"):
    print('Su usuario o contraseña son incorrectos')
else:
    print ('Bienvenido al sistema')
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

pregunta1 = int(input('Cual de los siguientes animales viven en el agua?\n 1)perro \n 2)cocodrilo \n 3)conejo \n 4)tiburon \n Ingrese el numero de su respuesta :'))
#if (pregunta1)


