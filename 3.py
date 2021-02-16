peso = float(input("Ingrese su peso: "))
altura= float(input("Ingrese su altura: "))

imc= peso / altura**2
if imc > 25:
    print("Tienes sobrepeso: ", imc)

if imc > 30:
    print("Tienes obesidad: ", imc)

if imc < 24.9:
    print("Tienes normopeso: ", imc)
    
if imc < 18.5: 
    print("Estas por debajo del peso", imc)

