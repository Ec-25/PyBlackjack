def menu():
    # diseño del menu
    menuini = """\n    =====================================================
    \t\tGoverno Of BlackJack v0.5.7
    =====================================================
    \t1) Crear Partida
    \t2) Cargar Partida
    \t3) Jugar
    \t4) Salir
    ====================================================="""
    print(menuini)
    # opcion a elejir del usuario
    opcion = 0
    # controlamos que solo ingrese numeros del 1 al 3
    while opcion not in (1, 2, 3, 4):
        try:
            opcion = int(input("OPCION = "))

        # controlamos que solo ingrese numeros
        except ValueError:
            pass

    # si es 3 colocamos -1 para finalizar el bucle del programa
    if opcion == 4:
        opcion = -1

    return opcion

def menu_seleccion_jugador(players):
    # diseño del menu de seleccion de jugador
    encabezado = """\n    =====================================================
    \t\tSeleccione su Jugador
    =====================================================
    """
    print(encabezado)
    # con los try, se garantiza que solo se imprimiran aquellos jugadores que existen
    print(">>>")

    # intenta imprimir todos los jugadores existentes
    for i in range(4):
        try:
            print(str(i+1), "-", players[i].name())

        except:
            # si el jugador no existe lo salta
            pass


    print("5- Salir")
    print("<<<")
    print("\n    =====================================================")

    # validacion de opcion
    jugador = -1
    while jugador not in (1, 2, 3, 4, 5):
        try:
            jugador = int(input("Jugador nro:  "))
            
            # checkeo de la validez de la opcion ingresada
            if jugador in (1, 2, 3, 4):
                try:
                    # con una bienvenida podemos determinar si el jugador existe
                    print("\nBienvenido/a", players[jugador-1].name())

                except:
                    # si no se imprime un mensaje de error
                    print("Error, El jugador no Existe.")
                    jugador = -1
            
            else:
                # si la opcion no existe se imprime el mensaje de error
                if jugador != 5:
                    print("Opcion Invalida")

        except ValueError:
            print("Error, Jugador Invalido.")

    # si es 5 colocamos 0 para volver al bucle del programa
    if jugador == 5:
        jugador = 0

    return jugador

def menu_jugar(players, playerID):
    # obtenemos el nombre del jugador
    idn = playerID - 1
    player = players[idn].name()
    
    opcion = -1
    while opcion not in (1, 2, 3, 4, 5):

        # diseño del menu
        print("\n    =====================================================", "\n\t\tBienvenido/a:", player, """\n    =====================================================
        1) Ingresar Fichas
        2) Jugar BlackJack
        3) Ver Estadisticas
        4) Guardar Partida
        5) Salir
    =====================================================""")

    # controlamos que solo ingrese numeros del 1 al 4
        try:
            opcion = int(input("OPCION = "))

            # control de seleccion de opcion
            if opcion not in (1, 2, 3, 4, 5):
                print("Opcion Invalida")

        # controlamos que solo ingrese numeros
        except ValueError:
            pass

    if opcion != 5:
        return opcion
    
    else:
        return 0

