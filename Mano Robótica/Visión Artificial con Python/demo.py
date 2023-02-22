# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Kenia Angulo Varela
# Juan de Dios Villa Carvajal
# Jesús Alfonso Rodríguez
# Ejercicio 15

# P es igual  potencia
# I es igual a corriente
# V es igual a voltaje
# R es igual a resistencia
R = 4
I = 0
P = 0
print ("Ingresa la cantidad de I que se va a utilizar: ", end = "")
I = float (input())
V = R * I 
print ("El voltaje total es de " + str(V) + " volts")
P = V * I
print ("La potencia total es de " + str(P) + " watts")