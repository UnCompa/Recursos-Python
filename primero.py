from colorama import Fore, Back, Style, init

# Inicializar Colorama (solo necesitas hacerlo una vez)
init()

# Solicitar al usuario que ingrese un número
numero = int(input('Ingrese un número: '))

# Imprimir la tabla de multiplicar con colores
for i in range(1, 11):
    res = numero * i

    # Colorear el texto según el resultado
    if res % 2 == 0:
        # Si el resultado es par, usar texto verde y fondo negro
        print(Fore.BLACK + f'{numero} * {i} = {res}' + Style.BRIGHT)
    else:
        # Si el resultado es impar, usar texto amarillo y fondo negro
        print(Fore.YELLOW + Back.BLACK + f'{numero} * {i} = {res}' + Style.RESET_ALL)
