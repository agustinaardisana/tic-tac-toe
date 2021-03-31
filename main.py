#crear tablero
# mostrar el tablero
# empezar el juego
#turnos
  #perdirle posicion al usuario
  #verificar que este libre
  #marcar esa posicion en el tablero
# verificar si hay ganador
  # ver si hay 3iguales en una fila
  # ver si hay 3iguales en una columna
  # ver si hay 3iguales en una diagonal
#verificar. sihay empate
#cambiar jugador  
  
tablero = ["-", "-", "-",
           "-", "-", "-", 
           "-", "-", "-"]

def mostrar_tablero():
  print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
  print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
  print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

mostrar_tablero()

seguir_jugando = True

jugador_activo = "⭕"

posicion = ""

ganador = None

def turno():
  global tablero, jugador_activo, posicion

  print("Es el turno de " + jugador_activo)

  posicion = ""

  valido = False

  while not valido:
    posicion = input("Elegi una posicion del 1 al 9: ")
    posicion = int(posicion) - 1

    if tablero[posicion] == "-":
      valido = True
    else:
      print("Posicion ocupada")

  tablero[posicion] = jugador_activo
  mostrar_tablero()

def verificar_columnas():
  global seguir_jugando, ganador

  col_1 = tablero[0] == tablero[3] == tablero[6] != "-"
  col_2 = tablero[1] == tablero[4] == tablero[7] != "-"
  col_3 = tablero[2] == tablero[5] == tablero[8] != "-"

  if col_1 == True or col_2 == True or col_3 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_filas():
  global seguir_jugando, ganador

  fila_1 = tablero[0] == tablero[1] == tablero[2] != "-"
  fila_2 = tablero[3] == tablero[4] == tablero[5] != "-"
  fila_3 = tablero[6] == tablero[7] == tablero[8] != "-"

  if fila_1 == True or fila_2 == True or fila_3 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_diagonal():
  global seguir_jugando, ganador

  diag_1 = tablero[0] == tablero[4] == tablero[8] != "-"
  diag_2 = tablero[2] == tablero[4] == tablero[6] != "-"

  if diag_1 == True or diag_2 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_empate():
  global seguir_jugando

  if "-" not in tablero:
    seguir_jugando = False

while seguir_jugando == True:
  turno()
  verificar_columnas()
  verificar_filas()
  verificar_diagonal()
  verificar_empate()

  if jugador_activo == "⭕":
    jugador_activo = "❌"
  else:
    jugador_activo = "⭕"

if ganador == "⭕" or ganador == "❌":
  print("El ganador es " + ganador)
else:
  print("Empate")
