opcion = input("Si desea convertir de Celsius a Fahrenheit (INGRESE FAHRE), si desea convertir de Fahrenheit a Celsius (INGRESE CELS): ")

if opcion == "FAHRE":
    celsius = float(input("Ingrese una temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura es igual a", fahrenheit, "grados Fahrenheit")

elif opcion == "CELS":
    fahrenheit = float(input("Ingrese una temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("La temperatura es igual a", celsius, "grados Celsius")

else:
    print("Ingrese una opción válida")
