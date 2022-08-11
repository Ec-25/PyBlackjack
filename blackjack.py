# Intento de Blackjack con 1 Crupier, hasta 4 Jugadores, y infinitas Rondas
import random


class Player:
    def __init__(self):
        # Estado inicial

        self.nombre = "player"

        # cantidad de fichas iniciales (modificable)
        self.chips = 1000

        # estadisticas
        self.wins = 0
        self.failed = 0
        self.natural21 = 0
        self.apuesta_maxima = 0
        self.fichas_maximas = 0

        # partida
        self.apuesta = 0
        self.points = 0

    def name(self):
        return self.nombre

    def change_name(self, nname):
        self.nombre = nname

    def subir_fichas(self, fichas):
        # ingresa las fichas colocadas
        self.chips += fichas

        # informa cuantas tiene disponible
        return self.chips

    def comprobar_fichas(self, gano):
        if gano + self.chips > self.fichas_maximas:
            self.fichas_maximas = gano + self.chips

    def iniciar_partida(self, apuesta):
        # se descuenta la apuesta inicial
        self.apuesta = apuesta
        self.chips -= apuesta

        # se contabiliza la apuesta maxima que ha tenido el jugador
        if apuesta > self.apuesta_maxima:
            self.apuesta_maxima = apuesta

        # se realiza la primera tirada de la mano y se informa
        carta, palo = self.tirar_carta()
        self.informar(carta, palo)
        # se realiza la segunda tirada de la mano y se informa
        carta, palo = self.tirar_carta()
        self.informar(carta, palo)

    def jugar(self):
        # se realiza una mano
        carta, palo = self.tirar_carta()
        self.informar(carta, palo)

    @staticmethod
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

    def informar(self, carta, palo):
        # imprimir en consola el resultado de la mano obtenida
        #   determinamos los puntos
        if carta == "A":
            if self.points + 11 <= 21:
                self.points += 11
            else:
                self.points += 1

        elif str(carta) in "JQK":
            self.points += 10

        else:
            self.points += carta

        if self.points != 0:
            # definimos el mensaje para cuando los puntos sean distintos de 0
            if str(carta) in "AJQK":
                print("Ha sacado la", carta, "de", palo, "sumando", self.points, "puntos")
            else:
                print("Ha sacado el", carta, "de", palo, "sumando", self.points, "puntos")

        else:
            # definimos el mensaje para cuando los puntos sean iguales a 0
            if str(carta) in "AJQK":
                print("Ha sacado la", carta, "de", palo)
            else:
                print("Ha sacado el", carta, "de", palo)

    def estadisticas(self):
        print("\n\t=====================================================\n")
        print("\tJugador:", self.nombre)
        print("\tCantidad de Victorias:", self.wins)
        print("\tCantidad de Derrotas:", self.failed)
        print("\tCantidad de veces conseguidas el 21 natural:", self.natural21)
        print("\tSu apuesta maxima fue:", self.apuesta_maxima)
        print("\tCantidad de Fichas Disponibles:", self.chips)
        print("\tMonto maximos de Fichas que ha logrado tener:", self.fichas_maximas)
        print("\n\t=====================================================")


def menu():
    # diseño del menu
    menuini = """\n    =====================================================
    \t\tBlacJack V2.0
    =====================================================
    \t1) Crear Jugador
    \t2) Jugar
    \t3) Salir
    ====================================================="""
    print(menuini)
    # opcion a elejir del usuario
    opcion = 0
    # controlamos que solo ingrese numeros del 1 al 3
    while opcion not in (1, 2, 3):
        try:
            opcion = int(input("OPCION = "))

        # controlamos que solo ingrese numeros
        except ValueError:
            pass

    # si es 3 colocamos -1 para finalizar el bucle del programa
    if opcion == 3:
        opcion = -1

    return opcion


def menu_sell_jugador():
    # diseño del menu de seleccion de jugador
    menujugador = """\n    =====================================================
    \t\tSeleccione su Jugador
    =====================================================
    """
    print(menujugador)
    # con los try, se garantiza que solo se imprimiran aquellos jugadores que existen
    print(">>>")
    try:
        print("1- ", player1.name())
    except NameError:
        pass

    try:
        print("2- ", player2.name())
    except NameError:
        pass

    try:
        print("3- ", player3.name())
    except NameError:
        pass

    try:
        print("4- ", player4.name())
    except NameError:
        pass

    print("5- Salir")
    print("<<<")
    print("\n    =====================================================")
    # validacion de opcion
    jug = -1
    while jug not in (1, 2, 3, 4, 5):
        try:
            jug = int(input("Jugador nro:\t\t"))

            if jug == 1:
                try:
                    # con una bienvenida podemos determinar si el jugador existe
                    print("\nBienvenido/a", player1.name())

                except NameError:
                    # si no se imprime un mensaje de error
                    print("Error, El jugador no Existe.")
                    jug = -1

            elif jug == 2:
                try:
                    print("\nBienvenido/a", player2.name())

                except NameError:
                    print("Error, El jugador no Existe.")
                    jug = -1

            elif jug == 3:
                try:
                    print("\nBienvenido/a", player3.name())

                except NameError:
                    print("Error, El jugador no Existe.")
                    jug = -1

            elif jug == 4:
                try:
                    print("\nBienvenido/a", player4.name())

                except NameError:
                    print("Error, El jugador no Existe.")
                    jug = -1

            else:
                # si la opcion no existe se imprime el mensaje de error
                if jug != 5:
                    print("Opcion Invalida")

        except ValueError:
            print("Error, Jugador Invalido.")

    # si es 5 colocamos 0 para volver al bucle del programa
    if jug == 5:
        jug = 0

    return jug


def menu_jugar(player):
    # obtenemos el nombre del jugador
    jugador = player
    if player == 1:
        nomb = player1.name()

    elif player == 2:
        nomb = player2.name()

    elif player == 3:
        nomb = player3.name()

    else:
        nomb = player4.name()

    opcion = -1
    while opcion != 0:

        # diseño del menu
        print("\n    =====================================================", "\n\t\tBienvenido/a:", nomb, """\n\t=====================================================
        1) Ingresar Fichas
        2) Jugar BJ
        3) Ver Estadisticas
        4) Salir
    =====================================================""")
        # opcion a elejir del usuario
        opcion = -1

        # controlamos que solo ingrese numeros del 1 al 4
        while opcion not in (1, 2, 3, 4):
            try:
                opcion = int(input("OPCION = "))

                # control de seleccion de opcion
                if opcion not in (1, 2, 3, 4):
                    print("Opcion Invalida")

            # controlamos que solo ingrese numeros
            except ValueError:
                pass

        # si es 4 colocamos 0 para volver al bucle del programa
        if opcion == 4:
            break

        if opcion == 1:
            # opcion de ingresar fichas
            ingresar_fichas(jugador)

        elif opcion == 2:
            # opcion de jugar
            print()

        elif opcion == 3:
            # opcion ver estadisticas
            ver_stats(jugador)


def crear_jugador():
    global players, player1, player2, player3, player4
    players = players + 1
    # creamos al nuevo jugador
    name = input("Seleccione un nombre:\t")
    # con un nombre que no supere los 16 caracteres
    while len(name) > 16:
        print("\nError, nombre no valido, Maximo 16 caracteres...")
        name = input("Seleccione un nombre:\t")

    # instanciamos al jugador y le asignamos nombre
    if players == 1:
        global player1
        player1 = Player()
        player1.change_name(name)

    elif players == 2:
        player2 = Player()
        player2.change_name(name)

    elif players == 3:
        player3 = Player()
        player3.change_name(name)

    elif players == 4:
        player4 = Player()
        player4.change_name(name)

    # solo se admiten 4 jugadores
    # si se supera se tendra que elejir a quien reemplazar
    else:
        print("\nError, demasiados Jugadores")
        print(">>>")
        print("1- ", player1.name())
        print("2- ", player2.name())
        print("3- ", player3.name())
        print("4- ", player4.name())
        print("5- Salir")
        print("<<<")
        print("\nElija una posicion para Reemplazar")

        # confirmacion de posicion valida para reemplazar jugador
        pos = 0
        while pos not in (1, 2, 3, 4, 5):
            try:
                if pos == -1:
                    print("\nError, Seleccione una posicion valida")

                pos = int(input("\t\t\t\t"))

            except ValueError:
                pos = -1
                pass

        # eliminamos al jugador antiguo, instanciamos al jugador nuevo y le asignamos nombre
        if pos == 1:
            del player1
            player1 = Player()
            player1.change_name(name)

        elif pos == 2:
            del player2
            player2 = Player()
            player2.change_name(name)

        elif pos == 3:
            del player3
            player3 = Player()
            player3.change_name(name)

        elif pos == 4:
            del player4
            player4 = Player()
            player4.change_name(name)

        else:
            pass

        players = 4


def ingresar_fichas(player):
    chips = -1
    while chips < 0 or chips > 100000:
        try:
            chips = int(input("Cantidad de Fichas\t"))

        except ValueError:
            pass

    if player == 1:
        print("La cantida de fichas que usted tiene es:", player1.subir_fichas(chips))

    elif player == 2:
        print("La cantida de fichas que usted tiene es:", player2.subir_fichas(chips))

    elif player == 3:
        print("La cantida de fichas que usted tiene es:", player3.subir_fichas(chips))

    elif player == 4:
        print("La cantida de fichas que usted tiene es:", player4.subir_fichas(chips))


def ver_stats(player):
    if player == 1:
        player1.estadisticas()

    elif player == 2:
        player2.estadisticas()

    elif player == 3:
        player3.estadisticas()

    elif player == 4:
        player4.estadisticas()


def program():
    # programa principal
    global players
    salir = 0
    players = 0

    while salir != -1:
        # imprimir menu y determinar que quiere realizar el jugador
        salir = menu()

        if salir == 1:
            # opcion crear jugdor nuevo
            crear_jugador()

        elif salir == 2:
            # jugar, seleccionar jugador, y luego preguntar monto a apostar, y empezar la partida

            # primero se selecciona 1 de los 4 jugadores disponibles
            player = menu_sell_jugador()
            # segundo base a ese jugador, lo que el jugador decida realizar
            if player != 0:
                menu_jugar(player)

            else:
                continue

    # salida
    exit("\nDone!")


if __name__ == "__main__":
    # comprobacion de ejecucion

    program()
