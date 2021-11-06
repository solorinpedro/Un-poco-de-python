dolar_euro = 0.91
libra_euro = 1.18

opcion = input("¿Que desea hacer ? \n"
               "A: Convertir de euro a dolar\n"
               "B: Convertir de dolar a euro\n"
               "C: Convertir de euro a libra\n"
               "D: Convertir de libra a euro\n")

texto_usuario = "Introduzca la cantidad de {} a convertir\n"

if opcion == "A":
    cantidad_de_Dinero = float(input(texto_usuario.format("euro")))
    print("La cantidad en dolar es: {}".format(cantidad_de_Dinero / dolar_euro))

elif opcion == "B":
    cantida_de_Dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad en euro es: {}".format(cantida_de_Dinero / dolar_euro))

elif opcion == "C":
    cantidad_de_Dinero = float(input(texto_usuario.format("euro")))
    print("La cantidad de dolar es: {}".format(cantidad_de_Dinero /euro_dolar))

elif opcion == "D":
    cantidad_de_Dinero = float(input(texto_usuario.format("lbra")))
    print("La cantidad de Libra es: {}".format(cantidad_de_Dinero * euro_libra))

else:
    print("Ha elegido una opcion incorrecta")
    exit()

