import string
import random

def generar_contraseña(longitud):
    if longitud < 4:
        print("La longitud debe ser al menos 4")
        return

    # Generar cada tipo de caracter y agregarlo a la contraseña
    contraseña = []
    contraseña.append(random.choice(string.ascii_uppercase))
    contraseña.append(random.choice(string.ascii_lowercase))
    contraseña.append(random.choice(string.digits))
    contraseña.append(random.choice(string.punctuation))

    # Rellenar el resto de la contraseña con caracteres aleatorios
    for i in range(longitud - 4):
        contraseña.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    # Mezclar la contraseña para que los primeros cuatro caracteres no sean predecibles
    random.shuffle(contraseña)

    # Convertir la lista a una cadena y devolverla
    return ''.join(contraseña)

longitud = int(input('Escribe el numero de caracteres deseados para tu contrasenna \n NOTA: el numero de caracteres debe ser mayor a cuatro: '))
print(generar_contraseña(longitud))