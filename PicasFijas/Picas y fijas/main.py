#Importar libreria random (randint)
from random import randint 

#Funcion para generar el numero a adivinar
def numero_secreto(cantidad): 
    secreto = []
    while True:
        d = randint(0, 9)
        if d not in secreto:
            secreto.append(d)
        if len(secreto) == cantidad:
            break
    return secreto

#Funcion para validar que el numero ingresado cumpla con los requerimientos
def validar_numero(numero): 
    if len(numero) == 1:
        return True
    else:
        if numero[0] in numero[1:]:
            return False
        else: 
            return validar_numero(numero[1:])

#Funcion que valida que la longitud coincida con el desafio aceptado
def validar_longitud(numero, longitud): 
    if len(numero) == longitud:
        return validar_numero(numero)
    else:
        return False

#Funcion principal donde se juega las picas y al tiempo se escribe los reslutados en un .txt
def multijugador():
  nombre = input("Nombre:")
  continuar = 1
  while continuar == 1:
    print("--------------------------------------------------------------------------")  
    print("Ingrese la dificultad\n 1 = Facil(3 digitos) \n 2 = Medio(4 digitos) \n 3 = Dificil(5 digitos): ")
    while True: 
      try:
        dificultad = int(input("Digita la dificultad del juego: "))
        break
      except:
        print("Error, digita de nuevo")
    print("--------------------------------------------------------------------------")  
    if (dificultad == 1):
      digitos = 3
      intentos = 10
      s = numero_secreto(digitos)
      continuar = 0
      print("Solo tienes 10 intentos. ")
      print(s)
    elif (dificultad == 2):
      digitos = 4
      intentos = 15
      s = numero_secreto(digitos)
      continuar = 0
      print("Solo tienes 15 intentos.")
      print(s)
    elif (dificultad == 3):
      digitos = 5
      intentos = 20
      s = numero_secreto(digitos)
      continuar = 0
      print("Solo tienes 20 intentos.")
      print(s)
    while True:
        numero = [int(x) for x in input("Ingrese un numero: ")]
        if validar_longitud(numero, digitos) == True:
            break           
        try:
            e = validar_longitud(numero, digitos)
            if e == False:
                quit()
        except:
            print("Ingrese un numero valido")
            continue
    f = open("Registros.txt", "a")
    final = comprobar(nombre, intentos, s, numero)
    f.write(str(final[0])+","+str(final[1])+","+str(final[2])+","+str(final[3]+"\n"))
    f.close()
    print(final)

#Aqui se escribe en el .txt cada resultado    
def comprobar(nombre, intentos, numero, entrada): 
    resultado = ""
    for i in range(intentos):
      fijas = 0
      picas = 0
      if intentos == 1:
        resultado = "Perdiste"
        print(resultado)
        intent = 0
        return [nombre, len(numero), intent, resultado]
      else:
        for i in range(len(entrada)):
          if numero[i] == entrada[i]:
            fijas = fijas + 1
          elif numero[i] in entrada:
            picas = picas + 1
          if fijas == len(entrada):
            resultado = "Ganaste"
            print(resultado)
            intent = intentos
            return [nombre, len(numero), intent, resultado]
        intentos = intentos-1
        print("Tienes", fijas, "fijas y", picas, "picas\n Intentos restantes: ", intentos)
        f = open("Registros.txt", "a")
        '''A diferencia de la escritura de un ganador perdedor: nombre,dificultad,intentos, mensaje.
        la escritura decada intento se da como: nombre,fijas,picas,intentos restantes.'''
        f.write(str(nombre) + "," + str(fijas) + "," + str(picas) + "," + str(intentos) + "\n")
        f.close()
        while True:
          entrada = [int(x) for x in input("Ingrese un numero: ")]
          if validar_longitud(entrada,len(numero)) == True:
            break           
          try:
            e = validar_longitud(entrada,len(numero))
            if e == False:
              quit()
          except:
            print("Ingrese un numero valido")
            continue

#Metodo para sacar a los ganadores / no sirve :c  
def records(record):
  archivo = open("Registros.txt","r")
  puntajes = []
  for i in archivo:
    i = i.rstrip()
    if not i.startswith(record):
      continue
    score = i.split(",")
    puntajes.append(score)
    puntaje = int(score[1])
    if(menor > puntaje):
      menor = puntaje
  for j in puntajes:
    menor=str(menor)
    if (j[1]==menor):
      print ("El mejor en ",record," digitos es:",j[3]," con ",j[1]," intentos")  

#Menu principal
print("Elija una opción:\n1) Jugar\n2) Records\n3) Salir\n")
opcion = input() 
if opcion == "1":
  multijugador()
elif opcion == "2":
  record = input("¿Que puntaje  quiere ver?\n3. para tres cifras\n4. para cuatro cifras\n5. para cinco cifras\n")
  records(record)
elif opcion == "3":
  exit()

  
