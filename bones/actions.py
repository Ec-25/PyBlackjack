from bones.players import *
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
    if plys in (1, 2, 3, 4):
        player = Player()
        player.change_name(name)

        players[plys-1] = player
        players.append(0)

    # solo se admiten 4 jugadores
    # si se supera se tendra que elejir a quien reemplazar
    else:
        print("\nError, demasiados Jugadores")
        print(">>>")
        print("1- ", players[0].name())
        print("2- ", players[1].name())
        print("3- ", players[2].name())
        print("4- ", players[3].name())
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
        if pos in (1, 2, 3, 4):
            # se crea el jugador
            player = Player()
            # se cambia el nombre
            player.change_name(name)
            # se lo guarda
            players[pos-1] = player

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
    while 0 >= chips or chips >= 100001:
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
        # hizo 21 natural por lo que se retorna lo pertinente
        return -1, False

    # primera tirada del crupier
    print("\n\tPrimera carta del Crupier")

    carta, palo = tirar_carta()
    
    if str(carta) in "AJQK":
        if str(carta) in "A":
            points_crupier = 11

            # si saca us As, se le da al jugador la oportunidad de apostar sobre seguro(si cree que el crupier puede hacer blackjack con su segunda carta, si gana sera recompensado con el doble de lo que aposto a seguro)
            de11 = True

        else:
            points_crupier = 10

            de11 = False

        print("\nHa sacado la", carta, "de", palo, "sumando", points_crupier, "puntos")
        
    else:
        points_crupier = carta
        print("\nHa sacado el", carta, "de", palo, "sumando", points_crupier, "puntos")

        de11 = False

    return points_crupier, de11

def jugar(players, playerID):
    # una tirada mas
    carta, palo = tirar_carta()
    player = players[playerID - 1].name()
    print("\n\tSiguiente carta de", player)

    # informar y contar puntos
    players[playerID - 1].informar(carta, palo)

    return  players[playerID - 1].puntos()

def tiradas_crupier(points_crupier, flag, players, playerID):
    print("\n=====================================================")
    print("\n\tAhora el Crupier Tirara las cartas que considere...")
    puntos_crupier = points_crupier
    
    if players[playerID - 1].puntos() < 18:
        bandera_desicion = True

    else:
        bandera_desicion = False

    # bucle de tiradas
    while puntos_crupier < 17 or (puntos_crupier < players[playerID - 1].puntos() and bandera_desicion):
        # tira una carta
        carta, palo = tirar_carta()

        # se determina su valor, lo que suma y se informa
        if str(carta) in "AJQK":
            if str(carta) in "A":

                # en el caso de que saque un A, se considera que si con esta suma mas de 21, esta solo valga 1
                if puntos_crupier + 11 >= 22:
                    puntos_crupier += 1

                else:
                    puntos_crupier += 11

            else:
                puntos_crupier += 10

            print("\nHa sacado la", carta, "de", palo, "sumando", puntos_crupier, "puntos")
            
        else:
            puntos_crupier += carta
            print("\nHa sacado el", carta, "de", palo, "sumando", puntos_crupier, "puntos")

        # si hay apuesta segura y su siguiente carta equivale a un 10 el jugador gana su apuesta segura
        if (str(carta) == "10" or str(carta) in "JQK" ) and flag == True:

            apuesta_segura = players[playerID - 1].ver_apuesta_segura()
            apuesta_segura *= 2

            # aplicamos ganancias
            players[playerID - 1].subir_fichas(apuesta_segura)

            nombre_player = players[playerID - 1].name()
            print("\n", nombre_player, "Ha ganado su Apuesta Segura.")

            # restablecemos su apuesta segura
            players[playerID - 1].asign_apuesta_segura(0)

            flag = False

        # pierde su apuesta segura
        elif flag == True:
            apuesta_segura = players[playerID - 1].ver_apuesta_segura()

            players[playerID - 1].bajar_fichas(apuesta_segura)

            # aplicamos perdidas
            nombre_player = players[playerID - 1].name()
            print("\n", nombre_player, "Ha perdido su Apuesta Segura.")

            # restablecemos su apuesta segura
            players[playerID - 1].asign_apuesta_segura(0)

            flag = False

    # el crupier se planta
    print("\n\tHasta Aqui. El Crupier se planta")

    return puntos_crupier

def juga_ganador(players, playerID, dinero_total):
    # se aplica
    players[playerID - 1].comprobar_fichas(dinero_total)
    players[playerID - 1].subir_fichas(dinero_total)
    # estadistica de victoria
    players[playerID - 1].victoria()
    # restablecer apuesta
    players[playerID - 1].asign_apuesta(0)

def juga_perdedor(players, playerID, dinero_total):
    # se aplica
    players[playerID - 1].bajar_fichas(dinero_total)
    # estadistica de derrota
    players[playerID - 1].derrota()
    # restablecer apuesta
    players[playerID - 1].asign_apuesta(0)

def final_mano(players, playerID, points_crupier, flag21natural):
    points_player = players[playerID - 1].puntos()
    apuesta_player = players[playerID - 1].ver_apuesta()
    comprobar_apuesta_maxima(players, playerID, apuesta_player)

    # blackjack natural del jugador
    if flag21natural:
        # ganancia
        dinero_total = apuesta_player * 3
        """
        # se aplica
        players[playerID - 1].comprobar_fichas(dinero_total)
        players[playerID - 1].subir_fichas(dinero_total)
        # estadistica de victoria
        players[playerID - 1].victoria()
        # restablecer apuesta
        players[playerID - 1].asign_apuesta(0)
        """
        # aplicar victoria general
        juga_ganador(players, playerID, dinero_total)

        # estadistica de 21 natural
        players[playerID - 1].natural_21()

        print("\nEnhorabuena!, BlackJack Natural de", players[playerID - 1].name(), " Y has ganado $",dinero_total)

        # restablecer puntos
        players[playerID - 1].res_puntos()

    # bj del jugador
    elif points_player == 21:
        # ganancia
        dinero_total = apuesta_player * 1.5
        # aplicar victoria general
        juga_ganador(players, playerID, dinero_total)

        print("\nEnhorabuena!, BlackJack de", players[playerID - 1].name(), "; has ganado $", dinero_total)

        # restablecer puntos
        players[playerID - 1].res_puntos()

    #bj del crupier
    elif points_crupier == 21:
        # perdida
        dinero_total = apuesta_player
        """
        # se aplica
        players[playerID - 1].bajar_fichas(dinero_total)
        # estadistica de derrota
        players[playerID - 1].derrota()
        # restablecer apuesta
        players[playerID - 1].asign_apuesta(0)
        """
        # aplicar derrota general
        juga_perdedor(players, playerID, dinero_total)

        print("\nQue Mala Suerte!, BlackJack del Crupier", "; Has perdido $", dinero_total)

        # restablecer puntos
        players[playerID - 1].res_puntos()
        

    # ninguno se paso
    elif points_player <= 21 and points_crupier <= 21:

        if points_player == points_crupier:
            # restablecer apuesta
            players[playerID - 1].asign_apuesta(0)

            print("\nHay Empate!, nadie pierde su apuesta!")

            # restablecer puntos
            players[playerID - 1].res_puntos()

        elif points_player > points_crupier:
            # ganancia
            dinero_total = apuesta_player
            # aplicar victoria general
            juga_ganador(players, playerID, dinero_total)

            print("\nGana el Jugador con", points_player, "puntos;", " Y gana $", dinero_total)

            # restablecer puntos
            players[playerID - 1].res_puntos()

        elif points_player < points_crupier:
            # perdida
            dinero_total = apuesta_player
            # aplicar derrota general
            juga_perdedor(players, playerID, dinero_total)

            print("\nGana el Crupier con", points_crupier, "puntos.", "\n\tHas perdido $", dinero_total)

            # restablecer puntos
            players[playerID - 1].res_puntos()


    # alguno se paso
    else:
        if points_player < 21:
            # ganancia
            dinero_total = apuesta_player
            # aplicar victoria general
            juga_ganador(players, playerID, dinero_total)

            print("\nEl crupier ha superado los 21 puntos. Gana", players[playerID - 1].name(), " $", dinero_total)

            # restablecer puntos
            players[playerID - 1].res_puntos()

        elif points_crupier < 21:
            # perdida
            dinero_total = apuesta_player
            # aplicar derrota general
            juga_perdedor(players, playerID, dinero_total)

            print("\nHas superado los 21 puntos. Gana el Crupier. Pierdes $", dinero_total)

            # restablecer puntos
            players[playerID - 1].res_puntos()

        else:
            # restablecer apuesta
            players[playerID - 1].asign_apuesta(0)

            # restablecer puntos
            players[playerID - 1].res_puntos()

            print("\nNadie Gana!. Ambos han Superado los 21 Puntos")

def asignar_apuesta(players, playerID):
    fichas_disponibles = players[playerID - 1].fichas()
    while True:
        try:
            # se solicita la apuesta
            monto = int(input("\nCuanto Apuestas: "))
            player = players[playerID - 1]

            # comprobar si la apuesta es valida para su cantidad de fichas
            if monto <= fichas_disponibles:
                player.asign_apuesta(monto)
                break

            else:
                print("\nTu apuesta supera tus fichas...")

        except:
            pass

def comprobar_apuesta_maxima(players, playerID, monto):
    # se comprueba si es la maxima
    if monto > players[playerID - 1].ver_apuesta_maxima():
        players[playerID - 1].n_apuesta_maxima(monto)
    
def doblar_apuesta(players, playerID):
    # obtenemos la cantidad de fichas disponibles
    fichas_disponibles = players[playerID - 1].fichas()
    apuesta_player = players[playerID - 1].ver_apuesta()

    # y verificamos si al duplicar su apuesta puede pagar
    if apuesta_player * 2 <= fichas_disponibles:
        monto = apuesta_player * 2
        # aplicamos su apuesta
        players[playerID - 1].asign_apuesta(monto)

        print("\nUsted ahora apuesta $", monto)

        return 0

    # en caso de que su apuesta supere sus fichas informamos
    else:
        print("No Dispone de Fichas Suficiente para doblar")

        return 1

def apostar_seguro(players, playerID):
    # obtenemos la cantidad de fichas disponibles
    fichas_disponibles = players[playerID - 1].fichas()

    # cuanto quiere pagar
    while True:
        try:
            # se solicita la apuesta a seguro
            monto = int(input("\nCuanto Apuestas: "))
            player = players[playerID - 1]

            if monto <= fichas_disponibles:
                player.asign_apuesta_segura(monto)
                break

            else:
                print("\nTu apuesta supera tus fichas...")
                # en caso de que su apuesta supere sus fichas informamos
                break

        except:
            pass