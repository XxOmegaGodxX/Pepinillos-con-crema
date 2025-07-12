import random

# Lista de caracteres válidos
elementalist = ['+', '9', '-', '/', '*', '!', '&', '$', '#', '?', '=', '@',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Pedir al usuario el tamaño
tamaño = int(input("¿Qué tantos caracteres quieres que tenga tu contraseña? "))

# Generar la contraseña
contraseña = ""
for i in range(tamaño):
    contraseña += random.choice(elementalist)

# Mostrar la contraseña generada
print("Tu contraseña generada es:", contraseña)


print("Las papayas dicen no sé")
