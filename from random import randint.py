from random import randint

print("¡BIENVENIDOS AL JUEGO DE ADIVINAR UN NÚMERO!")
print("El número estará entre el 1 y el 25")
print("¡Empecemos!")

r = randint(1, 25)
al= None
while al != r: 
 aleatorio = input("Escribe un número: ")
 al = int(aleatorio)

 if al < r: 
    print("El número correcto es mayor que tu intento.")

 elif al > r:
    print("El número correcto es menor que tu intento.")
    
print("¡Es correcto, felicidades!")





