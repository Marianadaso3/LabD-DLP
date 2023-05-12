class Notaciones:
    def __init__(self, infix):
        self.infix = infix # Se guarda la expresión regular en notación infix
        self.precedencia = {  # Diccionario que contiene la precedencia de cada operador
            '*': 3,
            '+': 3,
            '?': 3,
            '♣': 3,
            '•': 1,
            '|': 2,
            '(': 0,
            ')': 0,
            '': 0
        }

    

    #Función que agrega el operador de concatenación explícito "." donde sea necesario
    def concatenacion(self):
        infix = "" # Inicializar una cadena vacía para almacenar la cadena infix con operadores de concatenación explícitos agregados
        for i in range(len(self.infix)): # Iterar sobre la cadena infix original
            chr = self.infix[i]  # Obtener el carácter actual en la cadena infix
            infix += chr # Agregar el carácter a la nueva cadena infix
            #print ("VER ANTES DE CONCATENACION--" + infix)
            if i < (len(self.infix) - 1): # Verificar si se necesita agregar un operador de concatenación explícito después del carácter actual
                if (
                    ((chr in ')*+?') or (chr not in "?+()*•|\\'")) # Verificar si el carácter actual es un operador o un carácter válido
                    and (self.infix[i + 1] not in "+*?|)'") # Verificar si el siguiente carácter es un operador
                ):
                    infix += '•' # Agregar el operador de concatenación explícito a la nueva cadena infix
        #print ("VER CONCATENACION"+ infix)
        return infix # Devolver la cadena infix con los operadores de concatenación explícitos agregados

