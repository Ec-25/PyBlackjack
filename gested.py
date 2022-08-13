# Intento de Blackjack con 1 Crupier, hasta 4 Jugadores, y infinitas Rondas
from centro.playerclass import *
from centro.actions import *
from centro.gui import *


def main():
    # programa principal
    # variables fijas
    players = [0]
    opcion = 0

    while opcion != -1:
        # devuelve (1, 2, -1)
        opcion = menu()

        if opcion == 1:
            # opcion crear jugdor nueWvo
            players = crear_jugador(players)
            pass

        elif opcion == 2:
            # jugar, seleccionar jugador, y luego preguntar monto a apostar, y empezar la partida

            # primero se selecciona 1 de los 4 jugadores disponibles
            playerID = menu_seleccion_jugador(players)

            # segundo base a ese jugador, lo que el jugador decida realizar
            if playerID != 0:
                eleccion = -1
                while eleccion != 0:
                    eleccion = menu_jugar(players, playerID)
                    
                    if eleccion == 0:
                        # salir
                        break

                    elif eleccion == 1:
                        # ingresar fichas
                        ingresar_fichas(players, playerID)

                    elif eleccion == 2:
                        # apostar primero dinero
                        asignar_apuesta(players, playerID)

                        # empezar partida
                        flag21natural = False

                        points_crupier = iniciar_partida(players, playerID)

                        if points_crupier == -1:
                            flag21natural = True

                        # posibilidad de seguir jugando
                        puntos = 1
                        while puntos < 21:

                            # salimos del bucle si hay 21 natural
                            if flag21natural:
                                break

                            # preguntamos si quiere seguir jugando
                            desicion = -1
                            while desicion not in (0, 1):
                                try:
                                    desicion = int(input("\nQuieres seguir jugando?...[1 = Si ; 0 = No]\t"))

                                # con esto facilitamos el que si escribe el texto continue
                                except ValueError:
                                    pass
                            
                            # si elije seguir jugando
                            if desicion == 1:
                                puntos = jugar(players, playerID)

                            # corta el bucle para dejar de jugar
                            else:
                                break
                        
                        # el crupier tira las cartas que considere necesarias
                        if not flag21natural:
                            points_crupier = tiradas_crupier(points_crupier)

                        # interpretacion de la partida y estadisticas
                        final_mano(players, playerID, points_crupier, flag21natural)

                    elif eleccion == 3:
                        # ver estadisticas
                        ver_stats(players, playerID)

            else:
                # en el caso de que el playerID de 0, por lo que no exista ningun jugador
                continue

    # salida
    exit("\nDone!")

if __name__ == "__main__":
    # comprobacion de ejecucion
    main()
