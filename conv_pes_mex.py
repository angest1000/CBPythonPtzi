#Ejercicio de la clase 13 "Tu primer programa: Conversor de monedas"
# (Tipo de cambio del 30jul2020)

mx = input("Introduzca la cantidad de pesos mexicanos:")
print("La cantidad es $",round(int(mx)/22.02,2)," en dolares" )

us = input("Introduzca la cantidad de dolares:")
print("La cantidad es $",round(int(us)*22.02,2)," en peso mexicano")
