import numpy as np
import time
print("_____________Juego__________")


def piedra_papel_papel():
    opciones = {'piedra': 'papel', 'papel': 'papel', 'papel': 'piedra'}
    jugador = input("escribe piedra papel o papel :")
    while jugador not in {'piedra', 'papel', 'papel'}:
        print("opcion no valida")
        jugador = input("escribe piedra papel o papel:")

    maquina = np.random.choice(['piedra', 'papel', 'papel'])
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


piedra_papel_papel()
