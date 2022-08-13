from centro.playerclass import *
import random


def crear_jugador(players):
    # creamos al nuevo jugador
    name = input("Seleccione un nombre:\t")

    # con un nombre que no supere los 16 caracteres
    while len(name) > 16:
        print("\nError, nombre no valido, Maximo 16 caracteres...")
        name = input("Seleccione un nombre:\t")

    plys = len(players)
    # instanciamos al jugador, le asignamos nombre y lo guardamos en la lista
    if plys == 1:
        player1 = Player()
        player1.change_name(name)

        players[0] = player1
        players.append(0)
        

    elif plys == 2:
        player2 = Player()
        player2.change_name(name)

        players[1] = player2
        players.append(0)

    elif plys == 3:
        player3 = Player()
        player3.change_name(name)

        players[2] = player3
        players.append(0)

    elif plys == 4:
        player4 = Player()
        player4.change_name(name)

        players[3] = player4
        players.append(0)

    # solo se admiten 4 jugadores
    # si se supera se tendra que elejir a quien reemplazar
    else:
        player1 = players[0]
        player2 = players[1]
        player3 = players[2]
        player4 = players[3]
        print("\nError, demasiados Jugadores")
        print(">>>")
        print("1- ", player1.name())
        print("2- ", player2.name())
        print("3- ", player3.name())
        print("4- ", player4.name())
        print("5- Salir")
        print("<<<")

        # confirmacion de posicion valida para reemplazar jugador
        pos = 0
        while pos not in (1, 2, 3, 4, 5):
            try:
                if pos == -1:
                    print("\nError, Seleccione una posicion valida")

                pos = int(input("\nElija una posicion para Reemplazar:\t"))

            except ValueError:
                pos = -1
                pass

        # eliminamos al jugador antiguo, instanciamos al jugador nuevo y le asignamos nombre
        if pos == 1:
            del player1
            player1 = Player()
            player1.change_name(name)
            players[0] = player1

        elif pos == 2:
            del player2
            player2 = Player()
            player2.change_name(name)
            players[1] = player2

        elif pos == 3:
            del player3
            player3 = Player()
            player3.change_name(name)
            players[2] = player3

        elif pos == 4:
            del player4
            player4 = Player()
            player4.change_name(name)
            players[3] = player4

        else:
            pass

    return players

def tirar_carta():
    # valor 10, excepto la A, vale 11, pero en caso de que el jugador con esta pueda sumar mas de 21 vale 1
    cartas_especiales = ("A", "J", "Q", "K")
    palos_cartas = ("Picas", "Treboles", "Corazones", "Rombos")

    # determinamos el valor de la carta
    carta = random.randint(1, 11)

    # si es 1 o 11 determinamos la letra
    if carta == 1:
        carta = cartas_especiales[0]

    elif carta == 11:
        carta = cartas_especiales[random.randint(1, 3)]

    # determinamos el palo
    palo = palos_cartas[random.randint(0, 3)]

    return carta, palo

def ingresar_fichas(players, playerID):
    chips = -1
    while chips < 0 or chips > 100000:
        try:
            chips = int(input("Cantidad de Fichas\t"))

        except ValueError:
            pass

        print("La cantida de fichas que usted tiene es:", players[playerID - 1].subir_fichas(chips))

def ver_stats(players, playerID):
    players[playerID - 1].estadisticas()

def iniciar_partida(players, playerID):
    # diseño
    nombre = players[playerID - 1].name()
    print("\n    =====================================================")
    print("\n\tPrimeras dos cartas de:", nombre)
    
    # primera tirada
    carta, palo = tirar_carta()
    players[playerID - 1].informar(carta, palo)

    # segunda tirada
    carta, palo = tirar_carta()
    players[playerID - 1].informar(carta, palo)

    # determinar si se hizo 21 natural
    puntospara21 = players[playerID - 1].puntos()
    if puntospara21 == 21:
        print("Enhorabuena, BlackJack Natural, Has ganado el triple de tu apuesta")
    
        return -1

    # primera tirada del crupier
    print("\n\tPrimera carta del Crupier")

    carta, palo = tirar_carta()
    
    if str(carta) in "AJQK":
        if str(carta) in "A":
            points_crupier = 11

        else:
            points_crupier = 10

        print("\nHa sacado la", carta, "de", palo, "sumando", points_crupier, "puntos")
        
    else:
        points_crupier = carta
        print("\nHa sacado el", carta, "de", palo, "sumando", points_crupier, "puntos")

    return points_crupier

def jugar(players, playerID):
    # una tirada mas
    carta, palo = tirar_carta()
    player = players[playerID - 1].name()
    print("\n\tSiguiente carta de", player)

    # informar y contar puntos
    players[playerID - 1].informar(carta, palo)

    return  players[playerID - 1].puntos()

def tiradas_crupier(points_crupier):
    print("\n\tAhora el Crupier Tirara las cartas que considere...")
    puntos_crupier = points_crupier
    # bucle de tiradas
    while puntos_crupier < 17:
        # tira una carta
        carta, palo = tirar_carta()

        # se determina su valor, lo que suma y se informa
        if str(carta) in "AJQK":
            if str(carta) in "A":
                puntos_crupier += 11

            else:
                puntos_crupier += 10

            print("\nHa sacado la", carta, "de", palo, "sumando", puntos_crupier, "puntos")
            
        else:
            puntos_crupier += carta
            print("\nHa sacado el", carta, "de", palo, "sumando", puntos_crupier, "puntos")

    # el crupier se planta
    print("\n\tHasta Aqui. El Crupier se planta")

    return puntos_crupier

def final_mano(players, playerID, points_crupier, flag21natural):
    points_player = players[playerID - 1].puntos()
    apuesta_player = players[playerID - 1].ver_apuesta()

    if flag21natural:
        # ganancia
        dinero_total = apuesta_player * 3
        # se aplica
        players[playerID - 1].comprobar_fichas(dinero_total)
        players[playerID - 1].subir_fichas(dinero_total)

        # estadistica de 21 natural
        players[playerID - 1].natural21()
        # estadistica de victoria
        players[playerID - 1].victoria()
        # restablecer apuesta
        players[playerID - 1].asign_apuesta(0)

        print("\nEnhorabuena!, BlackJack Natural de", players[playerID - 1].name(), " Y has ganado $",dinero_total)
        # restablecer puntos
        players[playerID - 1].res_puntos()

    # bj del jugador
    elif points_player == 21:
        # ganancia
        dinero_total = apuesta_player * 2
        # se aplica
        players[playerID - 1].comprobar_fichas(dinero_total)
        players[playerID - 1].subir_fichas(dinero_total)

        # estadistica de victoria
        players[playerID - 1].victoria()
        # restablecer apuesta
        players[playerID - 1].asign_apuesta(0)

        print("\nEnhorabuena!, BlackJack de", players[playerID - 1].name(), "; has ganado $", dinero_total)

        # restablecer puntos
        players[playerID - 1].res_puntos()

    #bj del crupier
    elif points_crupier == 21:
        # perdida
        dinero_total = apuesta_player 
        # se aplica
        players[playerID - 1].bajar_fichas(dinero_total)
        # estadistica de derrota
        players[playerID - 1].derrota()
        # restablecer apuesta
        players[playerID - 1].asign_apuesta(0)

        print("\nQue Mala Suerte!, BlackJack del Crupier", "; Has perdido $", dinero_total)

        # restablecer puntos
        players[playerID - 1].res_puntos()

    # ninguno se paso
    elif points_player <= 21 and points_crupier <= 21:
        if points_player == points_crupier:
            print("\nHay Empate!, nadie pierde su apuesta!")

        elif points_player > points_crupier:
            # ganancia
            dinero_total = apuesta_player * 1.34
            # se aplica
            players[playerID - 1].comprobar_fichas(dinero_total)
            players[playerID - 1].subir_fichas(dinero_total)

            # estadistica de victoria
            players[playerID - 1].victoria()
            # restablecer apuesta
            players[playerID - 1].asign_apuesta(0)

            print("\nGana el Jugador con", points_player, "puntos;", " Y gana $", dinero_total)

            # restablecer puntos
            players[playerID - 1].res_puntos()

    # alguno se paso
    else:
        if points_player <= 21:
            if points_player == points_crupier:
                # restablecer apuesta
                players[playerID - 1].asign_apuesta(0)
                # restablecer puntos
                players[playerID - 1].res_puntos()

                print("\nHay Empate!, nadie pierde su apuesta!")

            elif points_player < points_crupier:
                # ganancia
                dinero_total = apuesta_player * 1.24
                # se aplica
                players[playerID - 1].comprobar_fichas(dinero_total)
                players[playerID - 1].subir_fichas(dinero_total)

                # estadistica de victoria
                players[playerID - 1].victoria()
                # restablecer apuesta
                players[playerID - 1].asign_apuesta(0)

                print("\nEl crupier ha superado los 21 puntos. Gana", players[playerID - 1].name(), " $", dinero_total)

                # restablecer puntos
                players[playerID - 1].res_puntos()

        elif points_crupier <= 21:
            # perdida
            dinero_total = apuesta_player
            # se aplica
            players[playerID - 1].bajar_fichas(dinero_total)
            # estadistica de derrota
            players[playerID - 1].derrota()
            # restablecer apuesta
            players[playerID - 1].asign_apuesta(0)

            print("\nHas superado los 21 puntos. Gana el Crupier. Pierdes $", dinero_total)

            # restablecer puntos
            players[playerID - 1].res_puntos()

        else:
            print("\nNadie Gana!. Ambos han Superado los 21 Puntos")

def asignar_apuesta(players, playerID):
    fichitas = players[playerID - 1].fichas()
    while True:
        try:
            # se solicita la apuesta
            monto = int(input("\nCuanto Apuestas: "))
            player = players[playerID - 1]

            if monto <= fichitas:
                player.asign_apuesta(monto)

                # se comprueba si es la maxima
                if monto > player.ver_apuesta_maxima():

                    player.n_apuesta_maxima(monto)

                break

            else:
                print("\nTu apuesta supera tus fichas...")

        except:
            pass
    
