import random

victorias_usuario = 0
victorias_maquina = 0
empates = 0
num_partida = 0

opciones = ["piedra", "papel", "tijera"]
opciones[0]

while True:
    
    
    print()
    ingreso = input("Escriba: Piedra, Papel, Tijera o S para salir ").lower()

    if ingreso == "s":
        break

    if ingreso not in ["piedra", "papel", "tijera"]:
        continue

    numero = random.randint(0,2)

    eleccion_maquina = opciones[numero]
    print()
    print("La máquina eligió: ",eleccion_maquina)

    num_partida += 1

    if ingreso == "piedra" and eleccion_maquina == "tijera" :
        print()
        print("Ganaste!")
        victorias_usuario += 1
        continue

    elif ingreso == "papel" and eleccion_maquina == "piedra" :
        print()
        print("Ganaste!")
        victorias_usuario += 1
        continue

    elif ingreso == "tijera" and eleccion_maquina == "papel" :
        print()
        print("Ganaste!")
        victorias_usuario += 1
        continue

    elif ingreso == "tijera" and eleccion_maquina == "tijera" :
        print()
        print("Empate!")
        empates += 1
        continue

    elif ingreso == "papel" and eleccion_maquina == "papel" :
        print()
        print("Empate!")
        empates += 1
        continue

    elif ingreso == "piedra" and eleccion_maquina == "piedra" :
        print()
        print("Empate!")
        empates += 1
        continue

    else:
        print()
        print("Perdiste!")
        victorias_maquina += 1

print()
print("Ganaste",victorias_usuario, "veces")
print("La máquina ganó",victorias_maquina, "veces")
print("Empataste",empates, "veces")
print("Jugaste",num_partida, "partidas")
print("Gracias por jugar!")
print()