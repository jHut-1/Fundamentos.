a = float(input('Digite el primer valor: '))
b = float(input('Digite el segundo valor: '))

print('''Escoja una opcion
1. Para suma
2. Para resta
3. Para multiplicacion
4. Division''')

opcion = int(input())

if opcion ==1:
    resultado = a+b
elif opcion ==2:
    resultado = a+b
elif opcion ==3:
    resultado = a*b
elif opcion ==4:
    resultado = a/b
elif opcion ==5:
    print('Esta opcion no existe')

print('El resultado de su operacion es: ', resultado)