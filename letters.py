
"""
Metodo que permite contar la cantidad de veces que esta una letra repetida en la frase o palabra
@param sentence Frase o palabra que se quiere contar
@return di Diccionario cuya llave representa la letra y su valor representa las repeticiones
"""

def countLetters(sentence):

    sentence = sentence.replace(" ", "")
    di = {}

    for i in range(len(sentence)):

        letter = sentence[i]
        count = sentence.count(sentence[i]) # Permite contar cuántas veces está la letra del índice i en la frase

        di[letter] = count

    return di

r = ''

while r != '0' :
   
   r = input('Ingrese la frase o palabra que desea contar o ingrese 0 para salir: ')

   if r != '0':
        print(countLetters(r))
   else:
        print("Saliendo...")