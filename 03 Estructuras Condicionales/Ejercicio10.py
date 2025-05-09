hemisferio = input("Elija la opción de en qué hemisferio se encuentra (N = Norte, S = Sur): ")
mes = int(input("Ingrese el mes actual (1-12): "))
dia = int(input("Ingrese el día actual (1-31): "))


if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
      print ("Usted se encuentra en invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <=20):
            print ("Usted se encuentra en primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            print ("Usted se encuentra en verano")
    else:
     print ("Usted está en otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
      print ("Usted se encuentra en verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <=20):
            print ("Usted se encuentra en otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            print ("Usted se encuentra en invierno")
else:
     print ("Usted está en primavera")

            


   

