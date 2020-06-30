def trans_1(estado,car):
	conjunto = set()
	if estado == 'A':
		if car == '1':
			conjunto.add('A')
			conjunto.add('C')
		elif car=='0':
			conjunto.add('A')
			conjunto.add('B')
	elif estado == 'B':
		if car == '0':
			conjunto.add('D')
	elif estado == 'C':
		if car == '1':
			conjunto.add('D')
	elif estado == 'D':
		if car == '1':
			conjunto.add('D')
		elif car == '0':
			conjunto.add('D')
	return conjunto
def AFND_1(conjunto,cadena,n):
	aux = set()
	if n+1>len(cadena):
		return conjunto
	else:
		for e in conjunto:
			aux = aux | trans_1(e,cadena[n])
			conjunto = aux
		return AFND_1(conjunto,cadena,n+1)
def trans_2(estado,car):
	conjunto = set()
	if estado == 'A':
		if car == '1':
			conjunto.add('A')
	elif estado == 'B':
		conjunto.add('A')
		conjunto.add('C')
	elif estado == 'C':
		if car == '0':
			conjunto.add('C')
			conjunto.add('D')
		elif car == '1':
			conjunto.add('C')
	return conjunto
def AFND_2(conjunto,cadena,n):
	aux = set()
	if n+1>len(cadena):
		return conjunto
	else:
		for e in conjunto:
			aux = aux | trans_2(e,cadena[n])
			conjunto = aux
		return AFND_2(conjunto,cadena,n+1)
def trans_3(estado,car):
	conjunto = set()
	if estado == 'A':
		if car == '1':
			conjunto.add('A')
		elif car=='0':
			conjunto.add('B')
	elif estado == 'B':
		if car == '1':
			conjunto.add('C')
		elif car=='0':
			conjunto.add('B')
	elif estado == 'C':
		if car == '0':
			conjunto.add('B')
		elif car=='1':
			conjunto.add('F')
			conjunto.add('D')
	elif estado == 'D':
		if car == '0':
			conjunto.add('F')
			conjunto.add('E')
	elif estado == 'E':
		if car=='1':
			conjunto.add('C')
		elif car=='0':
			conjunto.add('F')
	return conjunto
def AFND_3(conjunto,cadena,n):
	aux = set()
	if n+1>len(cadena):
		return conjunto
	else:
		for e in conjunto:
			aux = aux | trans_3(e,cadena[n])
			conjunto = aux
		return AFND_3(conjunto,cadena,n+1)
def trans_4(estado,car):
	conjunto = set()
	if estado == 'A':
		if car == '+':
			conjunto.add('B')
		elif car == '-':
			conjunto.add('B')
	elif estado == 'B':
		if car in dec:
			conjunto.add('B')
			conjunto.add('E')
		elif car=='.':
			conjunto.add('C')
	elif estado == 'C':
		if car in dec:
			conjunto.add('D')
	elif estado=='D':
		conjunto.add('F')
		if car in dec:
			conjunto.add('D')
	elif estado=='E':
		if car=='.':
			conjunto.add('D')	
	return conjunto
def AFND_4(conjunto,cadena,n):
    aux = set()
    if n+1>len(cadena):
        return conjunto
    else:
        for e in conjunto:
            aux = aux | trans_4(e,cadena[n])
        conjunto = aux
        return AFND_4(conjunto,cadena,n+1)
		
while True:
	print '\n1.- AFND 1.\n2.- AFND 2.\n3.- AFND 3.\n4.- AFND 4.\n5.- Salir.'
	opt=input('Selecciona una opcion: ')
	if opt==1:
		cadena = raw_input("Ingresa cadena: ")
		conjI = {'A'}
		valid = AFND_1(conjI,cadena,0)
		if 'D' in valid: print "Aceptada"
		else: print "No aceptada"
	elif opt==2:
		cadena = raw_input("Ingresa cadena: ")
		conjI = {'A','C'}
		valid = AFND_2(conjI,cadena,0)
		if 'A' in valid or 'D' in valid: print "Aceptada"
		else: print "No aceptada"
	elif opt==3:
		cadena = raw_input("Ingresa cadena: ")
		conjI = {'A'}
		valid = AFND_3(conjI,cadena,0)
		if 'F' in valid: print "Aceptada"
		else: print "No aceptada"
	elif opt==4:
		cadena = raw_input("Ingresa cadena: ")
		conjI = {'A','B'}
		dec={'0','1','2','3','4','5','6','7','8','9'}
		valid = AFND_4(conjI,cadena,0)
		if 'F' in valid: print "Aceptada"
		else: print "No aceptada"
	elif opt==5: break
	else: print 'Ingresa una opcion valida.'

