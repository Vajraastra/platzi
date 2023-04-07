import random

tu_marcador = 0
pc_marcador = 0
ronda = 1
opciones = ['piedra', 'papel', 'tijera']
tu_seleccion = None
pc_seleccion = None

print("Bienvenido al juego de piedra, papel o tijera")

while True:
    print("-"*20)
    print("Ronda", ronda)
    print("-"*20)
    tu_seleccion = input("Selecciona piedra, papel o tijera: ")
    pc_seleccion = random.choice(opciones)
    if tu_seleccion not in opciones:
        print("Tu seleccion no es valida")
        continue
    elif tu_marcador == 2:
        print("Ganaste el juego!")
        break
    elif pc_marcador == 2:
        print("Perdiste el juego!")
        break
    else:
        if tu_seleccion == pc_seleccion:
            print("Empate!")
            ronda += 1
            continue
        elif tu_seleccion == "piedra" and pc_seleccion == "tijera":
            print("Ganaste!")
            ronda += 1
            tu_marcador += 1
            continue
        elif tu_seleccion == "papel" and pc_seleccion == "piedra":
            print("Ganaste!")
            ronda += 1
            tu_marcador += 1
            continue
        elif tu_seleccion == "tijera" and pc_seleccion == "papel":
            print("Ganaste!")
            ronda += 1
            tu_marcador += 1
            continue
        elif tu_seleccion == "piedra" and pc_seleccion == "papel":
            print("Perdiste!")
            ronda += 1
            pc_marcador += 1
            continue
        elif tu_seleccion == "papel" and pc_seleccion == "tijera":
            print("Perdiste!")
            ronda += 1
            pc_marcador += 1
            continue
        elif tu_seleccion == "tijera" and pc_seleccion == "piedra":
            print("Perdiste!")
            ronda += 1
            pc_marcador += 1
            continue
