horas = int(input('Ingrese el numero de horas trabajadas: '))
valorh = float(input('Ingrese el valor por hora: '))

sueldo = horas * valorh
sueldod = sueldo * 0.08
sueldob = sueldo * 0.02
print('Su sueldo es de: ', sueldo - sueldod)
print('El valor descontado de sueldo en seguridad social es: ', sueldod)

if sueldo <300:
    print('Su sueldo con bonificacion es de: ', sueldo - sueldod + sueldob )