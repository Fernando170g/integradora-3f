import random

# Crear tablero vacío
tablero = [' ' for _ in range(9)]

def mostrar_tablero():
    print("\n   |   |   ")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print("   |   |   ")
    print("\nPosiciones:")
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")

def verificar_ganador():
    # Combinaciones ganadoras
    lineas = [
        [0,1,2], [3,4,5], [6,7,8],  # filas
        [0,3,6], [1,4,7], [2,5,8],  # columnas
        [0,4,8], [2,4,6]            # diagonales
    ]
    
    for linea in lineas:
        if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]] != ' ':
            return tablero[linea[0]]
    return None

def tablero_lleno():
    return ' ' not in tablero

def movimiento_usuario():
    print("\nTu turno (X):")
    posicion = int(input("Elige una posición (1-9): ")) - 1
    
    if tablero[posicion] == ' ':
        tablero[posicion] = 'X'
        return True
    else:
        print("Posición ocupada, elige otra.")
        return movimiento_usuario()

def movimiento_maquina():
    print("\nTurno de la máquina (O):")
    
    # Buscar posiciones libres
    posiciones_libres = [i for i in range(9) if tablero[i] == ' ']
    
    # Elegir posición aleatoria
    posicion = random.choice(posiciones_libres)
    tablero[posicion] = 'O'
    print(f"La máquina eligió la posición {posicion + 1}")

def jugar():
    print("¡Bienvenido al Ta-Te-Ti!")
    print("Tú eres X, la máquina es O")
    
    mostrar_tablero()
    
    while True:
        # Turno del usuario
        movimiento_usuario()
        mostrar_tablero()
        
        ganador = verificar_ganador()
        if ganador:
            print(f"\n¡Ganaste!" if ganador == 'X' else "\n¡La máquina ganó!")
            break
        
        if tablero_lleno():
            print("\n¡Empate!")
            break
        
        # Turno de la máquina
        movimiento_maquina()
        mostrar_tablero()
        
        ganador = verificar_ganador()
        if ganador:
            print(f"\n¡Ganaste!" if ganador == 'X' else "\n¡La máquina ganó!")
            break
        
        if tablero_lleno():
            print("\n¡Empate!")
            break

# Iniciar el juego
jugar()



