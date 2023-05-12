#Autor: Mariana David

#Importaciones
from yalex import *  
from utils import *
from simbolos import *


def encontrar_simbolo(simbolo,infixVar):
    if (simbolo in infixVar) | (simbolo == " "):
        if simbolo == " " or simbolo == "\t" or simbolo == "\n" or simbolo == "\s":
            return WHITESPACE
        elif simbolo == "if":
            return IF
        elif simbolo.isalnum() and simbolo[0].isalpha():
            return ID
        elif simbolo == "+":
            return PLUS
        elif simbolo == "*":
            return TIMES
        elif simbolo == "(":
            return LPAREN
        elif simbolo == ")":
            return RPAREN
        elif simbolo.isdigit():
            return NUMBER
        elif simbolo == ";":
            return SEMICOLON
        elif simbolo == "=":
            return ASSIGNOP
        elif simbolo == "<":
            return LT
        elif simbolo == "==":
            return EQ
        elif simbolo == "-":
            return MINUS
        elif simbolo == "/":
            return DIV
        elif simbolo == "|":
            return OR
        elif simbolo == ".":
            return IGNORE
        else:
            return ERROR
    return ERROR

if __name__ == "__main__": 
    y = Yalex()  # Se crea una instancia de la clase Yalex
    y.leerYalex('ArchivosYalex/slr-4.yal', True)  # Se lee un archivo yalex y se carga en la instancia de Yalex
    #print(y.infix)
    #print (y.specialtoks)
    print("Infix:\n", ''.join(y.conversionspecialtoks(y.infix)))
    infixVar =(''.join(y.conversionspecialtoks(y.infix)))
    print("Quedaria asi:",infixVar)
    with open('archivo.txt') as file:
        lines = file.readlines()
    #Se lee el txt y se guarda en una variable
    txt = open('archivo.txt','r')
    txtLines = txt.readlines()
    print("txtLines:",txtLines)
    #Se almacena cada linea del txt en una variable
    for line in txtLines:
        print("line:", line)
        for simbolo in line:
            print(encontrar_simbolo(simbolo, infixVar),":",simbolo)
            