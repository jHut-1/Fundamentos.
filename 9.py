print(''' Presione 1. para convertir a grados celsius farhenheit
presione 2. para convertir grados celsius a kelvin
''')
opcion = int(input())
grados = float(input('Ingrese los grados a convertir: '))

if opcion== 1:
    resultado = grados * 9 /5 + 32 
elif opcion ==2:
    resultado = (grados + 273.15)

print('El resultado es:', resultado)

