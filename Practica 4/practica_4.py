#!/usr/bin/env python
# -*- coding: utf-8 -*-
decimal = {"0","1","2","3","4","5","6","7","8","9"}
octal = {"0","1","2","3","4","5","6","7"}
hexadecimal = {"a","b","c","d","e","f","A","B","C","D","E","F"}
mm = {"+","-"}
aceptados = {1,12,5,6,8,11,2,3,15,13,18,19,17,16}
def AFDNUM(cadena):
    estado = 0
    for i in cadena:
        if estado == 0:
            if i in mm:
                estado = 1
            elif i in "<>=%/*!":
                estado = 15
            elif i == "0":
                estado = 3
            elif i in (decimal-{"0"}):
                estado = 6
            elif i in "$abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOÑPQRSTUV":
                estado = 19
            elif i in "()}{[].,;":
                estado = 16
            else:
                estado = -1
                break
        elif estado == 1:
            if i == "0":
                estado = 2
            elif i in (decimal-{"0"}):
                estado = 6
            elif i in "+-=":
                estado = 13
            else:
                estado = -1
                break
        elif estado == 2:
            if i in octal:
                estado = 12
            elif i == "x" or i == "X":
                estado = 4
            elif i == ".":
                estado = 7
            elif i in "89":
                estado = 14
            else:
                estado = -1
                break
        elif estado == 3:
            if i in octal:
                estado = 2
            elif i == "x" or i == "X":
                estado = 4
            elif i == ".":
                estado = 7
            else:
                estado = -1
                break
        elif estado == 4:
            if i in hexadecimal or i in decimal:
                estado = 5
            else:
                estado = -1
                break
        elif estado == 5:
            if i in hexadecimal or i in decimal:
                estado = 5
            else:
                estado = -1
                break
        elif estado == 6:
            if i in decimal:
                estado = 6
            elif i == ".":
                estado = 7
            elif i == "E":
                estado = 9
            else:
                estado = -1
                break
        elif estado == 7:
            if i in decimal:
                estado = 8
            else:
                estado = -1
                break
        elif estado == 8:
            if i in decimal:
                estado = 8
            elif i == "E":
                estado = 9
            else:
                estado = -1
                break
        elif estado == 9:
            if i in decimal:
                estado = 11
            elif i in mm:
                estado = 10
            else:
                estado = -1
                break
        elif estado == 10:
            if i in decimal:
                estado = 11
            else:
                estado = -1
                break
        elif estado == 11:
            if i in decimal:
                estado = 11
            else:
                estado = -1
                break
        elif estado == 12:
            if i in octal:
                estado = 12
            elif i in "89":
                estado = 14
            else:
                estado = -1
                break
        elif estado == 13:
            if True:
                estado = -1
                break
        elif estado == 14:
            if i in decimal:
                estado = 14
            elif i == ".":
                estado = 7
            else:
                estado = -1
                break
        elif estado == 15:
            if i == "=":
                estado = 13
            elif i == '/':
                estado = 17
            else:
                estado = -1
                break
        elif estado == 16:
            if True:
                estado = -1
                break
        elif estado == 17:
            if i in "0123456789 +-/*%<>=!$)\"\n([]}{-_.:,;~&$#\¡|°¬¿?!ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz":
                estado = 18
            else:
                estado = -1
                break
        elif estado == 18:
            if i in "01234 56789+-/*%<>=!$)\"\n([]}{-_.:,;~&$#\¡|°¬¿?!ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz":
                estado = 18
            else:
                estado = -1
                break
        elif estado == 19:
            if i in "0123456789abcdefghijklmnñopqrstuvwxyz$ABCDEFGHIJKLMNOÑPQRSTUV_":
                estado = 19
            else:
                estado = -1
                break

    if estado in aceptados:
        return True
    else:
        return False


def ComproN(i):
    val = False
    for j in " 0123456789+-/*%<>=!$ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz_()[]}{-.:,;~&#\¡¿|°¬?!":
        if i.startswith(j):
            val = True
    return val
archivo = open("clase.java", "r")

contador = 0
errores = set()

contenido = archivo.readlines()

for linea in contenido:
    contador += 1
    linea = linea.split(" ")
    lineaux = []
    for palabra in linea:
        simaux = ""
        for simbolo in palabra:
            if simbolo in ".()[];}{, /\n":
                simaux+=" "+simbolo+" "
            else:
                simaux += simbolo
        lineaux.append(simaux)
        lineaux = " ".join(lineaux)
        lineaux = lineaux.split(" ")
    #print(lineaux)
    for palaux in lineaux:
        if ComproN(palaux):
            if AFDNUM(palaux):
                continue
            else:
                errores.add(contador)
        else:
            continue

errores = sorted(list(errores))
if len(errores) > 0:
    for i in errores:
        print("Error en la linea: {}".format(i))
else:
    print("No hay errores")
#print("Numero de lineas: {}".format(len(contenido)))

archivo.close()
