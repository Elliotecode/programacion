import time

independiente_x = 0
dependiente_y = 0
control = 0
str_fl = "s"
tabla_x = []
tabla_y = []

while control == 0:
    independiente_x = float(input("escriba el valor independiente o X: "))
    if independiente_x <= 0:
        print("")
        print("oye, el valor no puede ser 0 o menor")
        time.sleep(3)
        exit()
    if isinstance(dependiente_y, str) == True:
        print("HEY, no puedes poner LETRAS aca")
        time.sleep(3)
        exit()

    dependiente_y = float(input("escriba el valor dependiente o Y: "))
    if independiente_x <= 0:
        print("")
        print("oye, el valor no puede ser 0 o menor")
        time.sleep(3)
        exit()
    if isinstance(dependiente_y, str) == True:
        print("HEY, no puedes poner LETRAS aca")
        time.sleep(3)
        exit()

    veces = int(input("cuantas veces se repite el dato: "))
    if isinstance(veces, float) == True:
        print("")
        print("no puede ser decimal")
        time.sleep(3)
        exit()
    if isinstance(veces, str) == True:
        print("")
        print("A, sos re troll")
        time.sleep(3)
        exit()
    if veces < 0:
        print("")
        print("te crees gracioso? no rompas mi programa")
        time.sleep(3)
        exit()

    else:
        constante_proporcionalidad = dependiente_y / independiente_x
        #sumar la lista
        for i in range(veces):
            tabla_x.append(independiente_x)
            independiente_x += 1
            tabla_y.append(dependiente_y)
        dependiente_y += constante_proporcionalidad
    #imprimir la tabla
        print("")
        print("Constante de proporcionalidad:", constante_proporcionalidad)
        print("")
        print("tabla de proporcionalidad")
        print("valores x", tabla_x)
        print("valores y", tabla_y)
        print("")
    
        time.sleep(3)
        repetir = str(input("desea reintroducir los datos? (s/n): "))
        if repetir == "n":
            control = 1
        elif repetir == "s":
            print("ok, reiniciando...")
            time.sleep(3)
            control = 0

salir = str(input("desea salir? (s/n): "))
if salir == "s":
    print("gracias por usar el programa")
    time.sleep(3)
    exit()
elif salir == "n":
    print("ok")
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
    time.sleep(9999)
        
else:
    print("bro...")
    time.sleep(3)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    time.sleep(0.1)
    exit()        
