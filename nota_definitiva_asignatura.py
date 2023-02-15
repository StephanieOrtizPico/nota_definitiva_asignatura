# Programa para calcular la nota definitiva de una asignatura en la Especialidad de Sistemas

print("-------------------------------------")
print("---- Calcular la nota Definitiva ----")
print("-------------------------------------")

# input
nc = int(input ("Digite el valor de la nota cognitiva: "))
np = int(input ("Digite el valor de la nota procedimental: "))
na = int(input ("Digite el valor de la nota actitudinal: "))
au = int(input ("Digite el valor de la autoevaluación: ")) 
bi = int(input ("Digite el valor de la nota bimestral: "))

# processing 
nd = (0.3*nc) + (0.3*np) + (0.1*na) +(0.1*au) +(0.1*bi)

# output
print("------------------------------")
print("--------- RESULTADOS ---------")
print("------------------------------")
print("La nota definitiva es " + str(nd))
