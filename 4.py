nota1 = float(input('Ingrese la nota del primer bimestre: '))
nota2 = float(input('Ingrese la nota del segundo bimestre: '))

promedio = (nota1 + nota2) /2 

if promedio <3.5:
    print("No aprobaste: ", promedio)

if promedio >3.5:
    print("Aprobaste: ",promedio)