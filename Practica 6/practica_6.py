def trans1(estado,car,pila):
    if estado == 'q0':
        if car == 'a' and pila[-1] == 'z':
            estado = 'q0'
            pila.append('a')
        elif car == 'a' and pila[-1] == 'a':
            estado = 'q0'
            pila.append('a')
        elif car == 'b' and pila[-1] == 'a':
            estado = 'q1'
            pila.append('b')
        else:
            estado = 'q4'
            pila.append('m')
    elif estado == 'q1':
        if car == 'c' and pila[-1] == 'b':
            estado = 'q2'
            pila.pop()
        else:
            estado = 'q4'
            pila.append('m')
    elif estado == 'q2':
        if car == 'c' and pila[-1] == 'a':
            estado = 'q3'
            pila.pop()
        else:
            estado = 'q6'
            pila.append('m')
    elif estado == 'q3':
        if car == 'c' and pila[-1] == 'a':
            estado = 'q3'
            pila.pop()
        elif car == 'c' and pila[-1] == 'z':
            estado = 'q3'
        else:
            estado = 'q4'
            pila.append('m')
    return estado
def AP1(estado,cadena,n,pila):
    if n+1>len(cadena):
        return estado
    else:
        estado = trans1(estado,cadena[n],pila)
        return AP1(estado,cadena,n+1,pila)
def trans2(estado,car,pila):
    if estado == 'q0':
        if car == '0' and pila[-1] == 'z':
            estado = 'q0'
            pila.append('a')
        elif car == '0' and pila[-1] == 'a':
            estado = 'q0'
            pila.append('a')
        elif car == '1' and pila[-1] == 'a':
            estado = 'q1'
            pila.pop()
        elif car == '3' and pila[-1] == 'z':
            estado = 'q4'
        else:
            estado = 'q6'
            pila.append('m')
    elif estado == 'q1':
        if car == '1' and pila[-1] == 'a':
            estado = 'q1'
            pila.pop()
        elif car == '1' and pila[-1] == 'z':
            estado = 'q2'
            pila.append('c')
        else:
            estado = 'q6'
            pila.append('m')
    elif estado == 'q2':
        if car == '1' and pila[-1] == 'c':
            estado = 'q2'
            pila.append('c')
        elif car == '2' and pila[-1] == 'c':
            estado = 'q3'
            pila.pop()
        else:
            estado = 'q6'
            pila.append('m')
    elif estado == 'q3':
        if car == '2' and pila[-1] == 'c':
            estado = 'q3'
            pila.pop()
        elif car == '3' and pila[-1] == 'z':
            estado = 'q4'
        elif len(pila) == 1 and pila[-1] == 'z':
            estado = 'q5'
            pila.append('d')
        else:
            estado = 'q6'
            pila.append('m')
    elif estado == 'q4':
        if car == '3' and pila[-1] == 'z':
            estado = 'q4'
    return estado
def AP2(estado,cadena,n,pila):
    if n+1>len(cadena):
        return estado
    else:
        estado = trans2(estado,cadena[n],pila)
        return AP2(estado,cadena,n+1,pila)
def trans3(estado,car,pila,pila2):
    conjunto = set()
    if estado == 'q0':
        if car == 'a' and pila[-1] == 'z' and pila2[-1] == 'z':
            pila.append('a')
            pila2.append('a')
            conjunto.add('q1')
            conjunto.add('q5')
    elif estado == 'q1':
        if car == 'a' and pila[-1] == 'a':
            pila.append('a')
            conjunto.add('q1')
        elif car == 'b' and pila[-1] == 'a':
            pila.append('b')
            conjunto.add('q2')
    elif estado == 'q2':
        if car == 'b' and pila[-1] == 'b':
            pila.append('b')
            conjunto.add('q2')
        elif car == 'c' and pila[-1] == 'b':
            pila.pop()
            conjunto.add('q3')
    elif estado == 'q3':
        if car == 'c' and pila[-1] == 'b':
            pila.pop()
            conjunto.add('q3')
        elif car == 'c' and pila[-1] == 'a':
            pila.pop()
            conjunto.add('q4')
    elif estado == 'q4':
        if car == 'c' and pila[-1] == 'a':
            pila.pop()
            conjunto.add('q4')
    elif estado == 'q5':
        if car == 'a' and pila2[-1] == 'a':
            conjunto.add('q6')
    elif estado == 'q6':
        if car == 'a' and pila2[-1] == 'a':
            pila2.append('a')
            conjunto.add('q5')
        elif car == 'b' and pila2[-1] == 'a':
            pila2.pop()
            conjunto.add('q7')
    elif estado == 'q7':
        if car == 'b' and pila2[-1] == 'a':
            pila2.pop()
            conjunto.add('q7')
    return conjunto
def APN3(conjunto,cadena,n,pila,pila2):
    aux = set()
    if n+1>len(cadena):
        return conjunto
    else:
        for e in conjunto:
            aux = aux | trans3(e,cadena[n],pila,pila2)
        conjunto = aux
        return APN3(conjunto,cadena,n+1,pila,pila2)
def trans4(estado,car,pila,pila2):
    conjunto = set()
    if estado == 'q0':
        if car == 'a' and pila[-1] == 'z' and pila2[-1] == 'z':
            pila.append('a')
            pila2.append('a')
            pila2.append('a')
            conjunto.add('q1')
            conjunto.add('q5')
    elif estado == 'q1':
        if car == 'a' and pila[-1] == 'a':
            pila.append('a')
            conjunto.add('q1')
        elif car == 'b' and pila[-1] == 'a':
            pila.append('b')
            conjunto.add('q2')
    elif estado == 'q2':
        if car == 'b' and pila[-1] == 'b':
            pila.append('b')
            conjunto.add('q2')
        elif car == 'c' and pila[-1] == 'b':
            pila.pop()
            conjunto.add('q3')
    elif estado == 'q3':
        if car == 'c' and pila[-1] == 'b':
            pila.pop()
            conjunto.add('q3')
        elif car == 'c' and pila[-1] == 'a':
            pila.pop()
            conjunto.add('q4')
    elif estado == 'q4':
        if car == 'c' and pila[-1] == 'a':
            pila.pop()
            conjunto.add('q4')
    elif estado == 'q5':
        if car == 'a' and pila2[-1] == 'a':
            pila2.append('a')
            pila2.append('a')
            conjunto.add('q5')
        elif car == 'b' and pila2[-1] == 'a':
            pila2.pop()
            conjunto.add('q6')
    elif estado == 'q6':
        if car == 'b' and pila2[-1] == 'a':
            pila2.pop()
            conjunto.add('q7')
    elif estado == 'q7':
        if car == 'b' and pila2[-1] == 'a':
            pila2.pop()
            conjunto.add('q6')
    return conjunto
def APN4(conjunto,cadena,n,pila,pila2):
    aux = set()
    if n+1>len(cadena):
        return conjunto
    else:
        for e in conjunto:
            aux = aux | trans4(e,cadena[n],pila,pila2)
        conjunto = aux
        return APN4(conjunto,cadena,n+1,pila,pila2)
def trans5(estado,car,pila):
    if estado == 'q1':
	if pila[-1] == 'x':
	    estado = 'q2'
        elif car == 'i' and pila[-1] == 'z':
            estado = 'q1'
            pila.append('z')
	elif car == 'e' and pila[-1] == 'z':
            estado = 'q1'
            pila.pop()
    return estado
def AP5(estado,cadena,n,pila):
    if n+1>len(cadena):
        return estado
    else:
        estado = trans5(estado,cadena[n],pila)
        return AP5(estado,cadena,n+1,pila)
		
while True:
	print '\n1.- AP 1.\n2.- AP 2.\n3.- APND 1.\n4.- APND 2.\n5.- AP 3.\n6.- Salir'
	opt=input('Selecciona una opcion: ')
	if opt==1:
		pila = ['z']
		cad = raw_input("Ingresa cadena: ")
		res = AP1('q0',cad,0,pila)
		if len(pila) == 1 and pila[-1] == 'z' and res == 'q3':
			print "Aceptada"
		else:
			print "No Aceptada"
	elif opt==2:
		pila = ['z']
		cad = raw_input("Ingresa cadena: ")
		res = AP2('q0',cad,0,pila)
		if len(pila) == 1 and pila[-1] == 'z' and res == 'q4':
			print("Aceptada")
		else:
			print "No Aceptada"

	elif opt==3:
		cadena = raw_input("Ingresa cadena: ")
		pila = ['z']
		pila2 = ['z']
		conjI = {'q0'}
		valid = APN3(conjI,cadena,0,pila,pila2)
		if len(pila) == 1 and pila[-1] == 'z' and 'q4' in valid:
			print "Aceptada"
		elif len(pila2) == 1 and pila2[-1] == 'z' and 'q7' in valid:
			print "Aceptada"
		else:
			print "No aceptada"
	elif opt==4:
		cadena = raw_input("Ingresa cadena: ")
		pila = ['z']
		pila2 = ['z']
		conjI = {'q0'}
		valid = APN4(conjI,cadena,0,pila,pila2)
		if len(pila) == 1 and pila[-1] == 'z' and 'q4' in valid:
			print("Aceptada")
		elif len(pila2) == 1 and pila2[-1] == 'z' and 'q7' in valid:
			print "Aceptada"
		else:
			print "No aceptada"
	elif opt==5:
		pila = ["x","z"]
		cad = raw_input("Ingresa cadena: ")
		res = AP5('q1',cad,0,pila)
		if len(pila) == 1 and pila[-1] == 'x':
			print "Las sentencias if y else no estan equilibradas"
		else:
			print "Las sentencias if y else estan equilibradas"
	elif opt==6: break
	else: print 'Ingresa una opcion valida.'
