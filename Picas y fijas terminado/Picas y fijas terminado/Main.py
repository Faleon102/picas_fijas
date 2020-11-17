from random import randint

def generar_secreto(cantidad): 
    secreto = []
    while True:
        d = randint(0, 9)
        if d not in secreto:
            secreto.append(d)
        if len(secreto) == cantidad:
            break
    return secreto

def validar_numero(numero): 
    if len(numero) == 1:
        return True
    else:
        if numero[0] in numero[1:]:
            return False
        else: 
            return validar_numero(numero[1:])

def validar_longitud(numero, longitud): 
    if len(numero) == longitud:
        return validar_numero(numero)
    else:
        return False

def puntaje(a):
    f = open("Registros.txt", "r")
    menor = 1000
    puntajes = []
    for i in f:
        i = i.rstrip()
        if not i.startswith(a):
            continue
        score = i.split(",")
        puntajes.append(score)
        puntaje = int(score[1])
        if(menor < puntaje):
            menor = puntaje
    for j in puntajes:
        menor = str(menor)
        if (j[1] == menor):
            print ("El mejor en ", a, " digitos es:", j[3], " con ", j[1], " intentos")

def comprobar(intentos, numero, entrada): 
    resultado = ""
    for i in range(intentos):
            fijas = 0
            picas = 0
            if intentos == 1:
                resultado = "Perdiste"
                print(resultado)
                intent = 0
                return [len(numero), intent, resultado]
            else:
                for i in range(len(entrada)):
                    if numero[i] == entrada[i]:
                        fijas = fijas + 1
                    elif numero[i] in entrada:
                        picas = picas + 1
                if fijas == len(entrada):
                    resultado = "Ganaste"
                    print(resultado)
                    intent = 11 - intentos
                    return [len(numero), intent, resultado]
                intentos = intentos-1
                print("tienes ", fijas, "fijas y tienes ", picas, "picas\n intentos restantes: ", intentos)
                f = open("Registros.txt", "a")
                f.write(str(fijas) + "," + str(picas) + "," + str(intentos) + "\n")
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


cifras = 0
intentos = 0

while True:
    opcion = input("Bienvenido al juego de picas y fijas. Porfavor elige una opcion:\n" 
    "a. Jugar en modo facil \nb. Jugar en modo normal  \nc. Jugar en modo Dificil \nd. Ver los mejores puntajes\n")
    if opcion == "a":
        print("Facil(3)")
        cifras = 3
        intentos = 10
        s = generar_secreto(cifras)

    elif opcion == "b":
        print("Normal(4)")
        cifras = 4
        intentos = 15
        s = generar_secreto(cifras)

    elif opcion == "c":
        print("Dificil(5)")
        cifras = 5
        intentos = 20
        s = generar_secreto(cifras)
        
    elif opcion == "d":
        a = input("¿Que puntaje  quiere ver?\n3. para tres cifras\n4. para cuatro cifras\n5. para cinco cifras\n")
        puntaje(a)
        break
    else:
        print("Fin del juego")
        break

    while True:
        n = [int(x) for x in input("Ingrese un numero: ")]
        if validar_longitud(n, cifras) == True:
            break           
        try:
            e = validar_longitud(n, cifras)
            if e == False:
                quit()
        except:
            print("Ingrese un numero valido")
            continue

    try:
        f = open("Registros.txt", "r")
        f.close()
    except:
        f = open("Registros.txt", "w")
        f.close()
    
    f = open("Registros.txt", "a")
    final = comprobar(intentos, s, n)
    nombre = input("Ingrese su nombre: ")
    final.append(nombre)
    f.write(str(final[0])+","+str(final[1])+","+str(final[2])+","+str(final[3]+"\n"))
    f.close()
    print(final)

