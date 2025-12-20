from random import randint
def mostrar_bienvenida():
   print("\n!BIENVENIDOS AL JUEGO DE ADIVINAR NUMEROS!")

   """Muestra el mensaje inicial del juego (OUTPUT)."""

def pedir_nombre():

   """Pide el nombre del jugador (INPUT) y lo devuelve."""

   nombre = input("Cual es tu nombre?").strip ()

    # .strip() elimina espacios al inicio y al final

   return nombre
   if nombre== "":
      nombre="Jugador"
      return nombre 
def elegir_dificultad():
   
   """ Muestra el menú de dificultad, valida la opción (SELECTION)
    y devuelve un diccionario con configuración (rango e intentos)."""
    
   niveles= {
      "1": { "nombre": "Facil", "rango": 10, "intentos": 6},
      "2": { "nombre": "Medio", "rango": 50, "intentos": 7},
      "3": { "nombre": "Dificil", "rango": 100, "intentos": 5}
   }
   while True: # repite hasta que el usuario elija bien
      print("\nElige un nivel de dificultad:")
      print("1) Facil (1-10, | 6 intentos)")
      print("2) Medio (1-50, | 7 intentos)")
      print("3) Dificil (1-100, | 5 intentos)")
      eleccion = input("Ingresa el numero correspondiente a la dificultad elegida: ")
      if eleccion in niveles: # Valida si la opción existe
         return niveles[eleccion]
      else:
         print("Eleccion invalida. Por favor, intenta de nuevo.") 
def pedir_numero(rango):
    """
    Pide un numero al usuario y valida: 
    -que sea un numero
    -que este dentro del rango permitido
    Devuelve el numero ya convertido a int.
    """

    while True:
      entrada= input(f"Adivina un numero entre 1 y {rango}: ").strip()
      if not entrada.isdigit():
         # Verifica si es un número entero positivo
         print("Debes escribir un numero (sin letras).")
         continue
      numero = int(entrada) # convierte el texto a número entero
      if 1 <= numero <= rango:
         return numero
      else:
         print(f"Fuera de rango. Debes elegir un numero entre 1 y {rango}.")
def jugar_partida(nombre, config):

   """
    Ejecuta una partida completa del juego:
    - genera número secreto
    - controla intentos
    - da pistas
    - determina ganar/perder
    Devuelve True si ganó, Falso si perdió.
    """

   rango= config["rango"]
   intentos= config["intentos"]
   numero_secreto = randint(1, rango)  # número aleatorio según dificultad

   print(f"\n{nombre}, nivel {config['nombre']}. !Suerte!")
   print(f"Tienes {intentos} intentos.\n")
   while intentos > 0:
      intento= pedir_numero(rango)
      if intento == numero_secreto:
         print(f"Felicidades, ganaste!\n")
         return True
      if intento < numero_secreto:
            print(" Pista: El número secreto es MAYOR.")
      else:
            print(" Pista: El número secreto es MENOR.")

      intentos -= 1  # se descuenta un intento
      print(f"Intentos restantes: {intentos}\n")

    # Si salió del bucle, se quedó sin intentos
      print(f"Perdiste. El número era: {numero_secreto}\n") 
      return False


def preguntar_reinicio():
    """Pregunta si desea reiniciar (INPUT) y devuelve True/False."""
    while True:
        op = input("¿Deseas jugar otra vez? (S/N): ").strip().upper()
        # .upper() convierte a mayúscula para aceptar s/S y n/N

        if op == "S":
            return True
        elif op == "N":
            return False
        else:
            print("Responde con S o N.")


def main():
    """
    Función principal: controla el flujo general del programa.
    """
    mostrar_bienvenida() 

    nombre = pedir_nombre()  
    seguir = True

    while seguir: 
        config = elegir_dificultad()  

        jugar_partida(nombre, config)  

        seguir = preguntar_reinicio()

    print("\nGracias por jugar. ¡Hasta pronto!\n")  


# Esto hace que el programa comience aquí cuando ejecutas el archivo:
if __name__ == "__main__":
    main()

