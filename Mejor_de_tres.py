
numero1 = int(input("Introduzca el primer numero: "))
numero2 = int(input("Introduzca el segundo numero: "))
numero3 = int(input("Introduzca el tercer numero: "))

print("El numero mas grande entre {}, {} y {} es:{}, y el mas pequeño es: {}".format(numero1,numero2,numero3,
                                                                                    max(numero1,numero2,numero3),
                                                                                    min(numero1,numero2,numero3)))