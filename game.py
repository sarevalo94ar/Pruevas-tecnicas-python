import numpy as np
import time
print("_____________Juego__________")


def piedra_tijera_papel():
    opciones = {'piedra': 'tijera', 'tijera': 'papel', 'papel': 'piedra'}
    jugador = input("escribe piedra papel o tijera :")
    while jugador not in {'piedra', 'tijera', 'papel'}:
        print("opcion no valida")
        jugador = input("escribe piedra papel o tijera:")

    maquina = np.random.choice(['piedra', 'papel', 'tijera'])
    time.sleep(.4)
    print("\n Has selecionado :", jugador)
    print("La computadora ha selecionado", maquina)
    time.sleep(2)
    if opciones[jugador] == maquina:
        print("Has ganado")
    elif opciones[maquina] == jugador:
        print("!Has perdido")
    else:
        print("empate")


piedra_tijera_papel()
