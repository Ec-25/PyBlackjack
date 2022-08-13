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

    def puntos(self):
        return self.points

    def ver_apuesta(self):
        return self.apuesta

    def asign_apuesta(self, monto):
        self.apuesta = monto

    def fichas(self):
        return self.chips

    def change_name(self, nname):
        self.nombre = nname

    def subir_fichas(self, fichas):
        # ingresa las fichas colocadas
        self.chips += fichas

        # informa cuantas tiene disponible
        return self.chips

    def bajar_fichas(self, fichas):
        # ingresa las fichas colocadas
        self.chips -= fichas

        # informa cuantas tiene disponible
        return self.chips

    def comprobar_fichas(self, gano):
        if gano + self.chips > self.fichas_maximas:
            self.fichas_maximas = gano + self.chips

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
                print("\nHa sacado la", carta, "de", palo, "sumando", self.points, "puntos")
            else:
                print("\nHa sacado el", carta, "de", palo, "sumando", self.points, "puntos")

        else:
            # definimos el mensaje para cuando los puntos sean iguales a 0
            if str(carta) in "AJQK":
                print("\nHa sacado la", carta, "de", palo)
            else:
                print("\nHa sacado el", carta, "de", palo)

    def estadisticas(self):
        print("\n\t=====================================================\n")
        print("\tJugador:", self.nombre)
        print("\tCantidad de Victorias:", self.wins)
        print("\tCantidad de Derrotas:", self.failed)
        print("\tCantidad de veces conseguidas el 21 natural:", self.natural21)
        print("\tSu apuesta maxima fue: $", self.apuesta_maxima)
        print("\tCantidad de Fichas Disponibles: $", self.chips)
        print("\tMonto maximos de Fichas que ha logrado tener: $", self.fichas_maximas)
        print("\n\t=====================================================")

    def ver_apuesta_maxima(self):
        return self.apuesta_maxima

    def n_apuesta_maxima(self, monto):
        self.apuesta_maxima = monto

    def natural21(self):
        self.natural21 += 1

    def victoria(self):
        self.wins += 1

    def derrota(self):
        self.failed += 1

    def res_puntos(self):
        self.points = 0
    
