import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
        #Seleccionar una palabra al azar de la lista
        palabra = random.choice(palabras)
        #Filtro de palabras por caracter
        while '-' in palabra or ' ' in palabra:
                palabra = random.choice(palabras)

        return palabra.upper()
def ahorcado():
        print(' Bienvenido al ahorcado! ')

        palabra = obtener_palabra_valida(palabras)

        #Llamamos a set para crear un conjunto (lista de caracteres que no se repiten)
        letras_por_adivinar = set(palabra)
        letras_adivinadas = set()
        abecedario = set(string.ascii_uppercase)

        vidas = 7

        while len (letras_por_adivinar) > 0 and vidas > 0:
                print(f"Te quedan {vidas} vidas y has utilizado estas letras: {' '.join(letras_adivinadas)}")

                # Mostrar el estado actual de la palabra
                palabra_lista = [letra if letra in letras_adivinadas
                                 else '-' for letra in palabra]
                # Mostrar estado de la horca
                print (vidas_diccionario_visual[vidas])
                # Mostrar letras separadas por el espacio
                print (f"Palabra: {''.join(palabra_lista)}")

                # Ingreso por el usuario
                letra_usuario = input ("Escoge una letra: ").upper()

                # Si la letra escogida por el usuario no esta repetida pero si esta en el abecedario
                # Se agrega la letra a las las adivinadas
                if letra_usuario in abecedario - letras_adivinadas:
                        letras_adivinadas.add(letra_usuario)

                        # Si la letra esta en la palabra
                        # quitar la letra del conjunto de letras pendientes por adividnar
                        # Si no esta en la palabra quitar una vida
                        if letra_usuario in letras_por_adivinar:
                                letras_por_adivinar.remove(letra_usuario)
                                print('')
                        else:
                                vidas = vidas -1
                                print(f"\nLa letra, {letra_usuario} no esta en la palabra.")
                # Si la letra elegida ya fue ingresada
                elif letra_usuario in letras_adivinadas:
                        print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
                else:
                        print("\nEsta letra no es valida.")
        # Cuando se adivinan todas las letras de las palabras o cuando se terminan las vidas
        if vidas == 0:
                print(vidas_diccionario_visual[vidas])
                print(f"Perdiste y fuiste ¡Ahorcado!. La palabra era: {palabra}")
        else:
                print(f"¡Exelente! ¡La palabra efectivamente era {palabra} no seras ahorcado por ahora! ᕙ(^▿^-ᕙ)")

if __name__ == '__main__':
    ahorcado()