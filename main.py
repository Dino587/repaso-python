print("Hola mundo")
print("Hola mundo")

#soy duende de loco
print("Hola mundo")

"""
Texto que no se va a interpretar, va serios
Texto que no se va a interpretar, va serios
Texto que no se va a interpretar, va serios
"""

#Variables

texto = "Repaso de Python"
nombre = "DINO"
altura = "192cm"
year = 2023

print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

# Entrada
#sitioweb = input("¿Cuál es tu página web?: ")
#print("el sitio web del usuario es: " + sitioweb)

# Condiciones
"""
altura = int(input("¿Cuál es tu altura?: "))
if altura >= 180:
    print("Eres una persona alta!!")
else:
    print("Eres bajito")
"""

# Funciones
"""
var_altura = int(input("¿Cuál es tu altura?: "))

def mostrarAltura(altura):
    resultado = " "

    if altura >= 180:
        resultado = "Eres una persona alta!!"
    else:
        resultado = "Eres bajito"

    return resultado

print(mostrarAltura(var_altura))
"""

# Listas
personas = ["Víctor", "Paco", "Pepe"]

print(personas[2])

for persona in personas:
    print("-" + persona)