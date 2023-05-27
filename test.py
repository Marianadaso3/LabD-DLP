
# This Python file uses the following encoding: utf-8

# Importamos el automata
import direct_afd
import utils
import draw

# Extraemos los tokens
tks = {
    "WHITESPACE":'˂\\s°\\t°\\n˃♦',
   "ID":'˂A°B°C°D°E°F°G°H°I°J°K°L°M°N°O°P°Q°R°S°T°U°V°W°X°Y°Z°a°b°c°d°e°f°g°h°i°j°k°l°m°n°o°p°q°r°s°t°u°v°w°x°y°z˃˂˂A°B°C°D°E°F°G°H°I°J°K°L°M°N°O°P°Q°R°S°T°U°V°W°X°Y°Z°a°b°c°d°e°f°g°h°i°j°k°l°m°n°o°p°q°r°s°t°u°v°w°x°y°z˃°˂0°1°2°3°4°5°6°7°8°9˃˃♣',
   "PLUS":'+',
   "TIMES":'*',
   "LPAREN":'(',
   "RPAREN":')',
   }
chars = []

# Extraemos todos los posibles caracteres de la gramatica Ej. (a, b, c, 1, 2, 3, =, +, etc)
for k, v in tks.items():
    # Se itera sobre los elementos de cada valor (lista) en el diccionario 'tks'
    for j in v:
        # Se verifica si el elemento 'j' no está presente en la cadena de caracteres "˂˃°☺♣►♦"
        # y tampoco está en la lista 'chars'
        if j not in "˂˃°☺♣►♦" and j not in chars:
            # Si cumple las condiciones anteriores, se agrega 'j' a la lista 'chars'
            chars.append(j)
    
# Generamos una expresion regular infix completa al cocatenar las expresiones individuales de cada token
# El simbolo ↑ nos indica el final de la expresion regular, nos servira para determinar estados de aceptacion
cadena = "°".join(["˂˂" + t + "˃↑˃" for t in tks.values()])

# Se pide el archivo a analizar
name_file = input("Ingrese el nombre del archivo: ")
file = open(name_file, "r", encoding= "utf-8")

# Se obtienen todas las lineas a evaluar
text_to_scan = "".join(file.readlines())

# Se crea el automata con la expresion regular general, caracteres extraidos y el listado de nombres de identificadores
dir_afd = direct_afd.direct_afd(cadena, chars, [t for t in tks.keys()])

# Generar grafico
estados = {state.idx for state in dir_afd.states}
primer_estado = dir_afd.init_state
aceptacion = {state[0] for state in dir_afd.accept_states}
trans_func = draw.trans_func_afd(dir_afd.transitions)

print("Estados del AFN: ", estados)
print("Primer estado: ", primer_estado)
print("Estados de aceptacion: ", aceptacion)
print("Tabla de transiciones: ", trans_func)

#Grafico
draw.local_graph(estados, primer_estado, aceptacion, trans_func, "Direct-AFD")

# Se realiza la simulacion, se comienza por el indice 0
actual_pos = 0
while actual_pos < len(text_to_scan):
    # La posicion actual se va actualizando cada que se encuentra o no un token
    # Res es la cadena que se evaluo en ese momento
    # Si acept trae un valor es que llego a un estado de aceptacion y se devuelve su respectivo identificadors
    res, actual_pos, acept = dir_afd.simulate_afd(text_to_scan, actual_pos)
    if acept:
        print(" -", repr(res).strip(), "es ", dir_afd.tokens[acept])
        continue
    # En caso de no encontrar estado de aceptacion
    else:
        if res != "":
            print(" -", repr(res).strip(), "es un simbolo NO es reconocido")

