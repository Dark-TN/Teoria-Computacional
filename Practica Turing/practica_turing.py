global tamano_cinta
tamano_cinta=100

def borrar_blanco(cinta):
	cadena=[]
	for i in cinta: 
		if i != 'b': cadena.append(i)
	return ''.join(cadena)
def duplicador_unos():
	estado='p'
	cinta=[]
	for i in range(tamano_cinta): cinta.append('b')
	palabra=raw_input('Inserta una cadena de unos: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado!='s':
		if estado=='p':
			if cinta[c]=='1':
				estado='q'
				cinta[c]='0'
				c+=1
			elif cinta[c]=='0':
				c-=1
			elif cinta[c]=='b':
				estado='r'
				c+=1
		elif estado=='q':
			if cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
			elif cinta[c]=='b':
				estado='p'
				cinta[c]='0'
				c-=1
		elif estado=='r':
			if cinta[c]=='0':
				cinta[c]='1'
				c+=1
			elif cinta[c]=='b':
				estado='s'
	print borrar_blanco(cinta)
def complemento_binario():
	estado='q0'
	cinta=[]
	for i in range(tamano_cinta): cinta.append('b')
	palabra=raw_input('Inserta una cadena binaria: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado!='q1':
		if estado=='q0':
			if cinta[c]=='0':
				cinta[c]='1'
				c+=1
			elif cinta[c]=='1':
				cinta[c]='0'
				c+=1
			elif cinta[c]=='b':
				estado='q1'
				c-=1
	print borrar_blanco(cinta)
def paridad():
	estado='q0'
	cinta=[]
	for i in range(tamano_cinta): cinta.append('b')
	palabra=raw_input('Inserta una cadena binaria: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado!='q2':
		if estado=='q0':
			if cinta[c]=='0':
				c+=1
			elif cinta[c]=='1':
				estado='q1'
				c+=1
			elif cinta[c]=='b':
				estado='q2'
				cinta[c]='0'
				c-=1
		elif estado=='q1':
			if cinta[c]=='0':
				c+=1
			elif cinta[c]=='1':
				estado='q0'
				c+=1
			elif cinta[c]=='b':
				estado='q2'
				cinta[c]='1'
				c-=1
	print borrar_blanco(cinta)
def espejo():
	estado='q0'
	cinta=[]
	for i in range(tamano_cinta): cinta.append('b')
	palabra=raw_input('Inserta una cadena binaria: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado!='q13':
		if estado=='q0':
			if cinta[c]=='b':
				estado='q1'
				c-=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
		elif estado=='q1':
			if cinta[c]=='b':
				estado='q8'
				c+=1
			elif cinta[c]=='1':
				estado='q2'
				cinta[c]='#'
				c+=1
			elif cinta[c]=='0':
				estado='q5'
				cinta[c]='#'
				c+=1
		elif estado=='q2':
			if cinta[c]=='b':
				estado='q3'
				c+=1
			elif cinta[c]=='1':
				estado='q2'
				c+=1
			elif cinta[c]=='0':
				estado='q2'
				c+=1
		elif estado=='q3':
			if cinta[c]=='b':
				estado='q4'
				cinta[c]='1'
				c-=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
		elif estado=='q4':
			if cinta[c]=='b':
				c-=1
			elif cinta[c]=='1':
				c-=1
			elif cinta[c]=='0':
				c-=1
			elif cinta[c]=='#':
				estado='q1'
				cinta[c]='1'
				c-=1
		elif estado=='q5':
			if cinta[c]=='b':
				estado='q6'
				c+=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
		elif estado=='q6':
			if cinta[c]=='b':
				estado='q7'
				cinta[c]='0'
				c-=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
		elif estado=='q7':
			if cinta[c]=='b':
				c-=1
			elif cinta[c]=='1':
				c-=1
			elif cinta[c]=='0':
				c-=1
			elif cinta[c]=='#':
				estado='q1'
				cinta[c]='0'
				c-=1
		elif estado=='q8':
			if cinta[c]=='b':
				estado='q9'
				c+=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
		elif estado=='q9':
			if cinta[c]=='b':
				estado='q13'
				c-=1
			elif cinta[c]=='1':
				estado='q10'
				cinta[c]='b'
				c-=1
			elif cinta[c]=='0':
				estado='q11'
				cinta[c]='b'
				c-=1
		elif estado=='q10':
			if cinta[c]=='b':
				estado='q12'
				cinta[c]='1'
				c+=1
		elif estado=='q11':
			if cinta[c]=='b':
				estado='q12'
				cinta[c]='0'
				c+=1
		elif estado=='q12':
			if cinta[c]=='b':
				estado='q9'
				c+=1
	print borrar_blanco(cinta)
def parentesis():
	estado='q0'
	cinta=[]
	for i in range(tamano_cinta): cinta.append('b')
	palabra=raw_input('Inserta una cadena de parentesis: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado!='q6':
		if estado=='q0':
			if cinta[c]=='(':
				c+=1
			elif cinta[c]==')':
				estado='q1'
				cinta[c]='X'
				c-=1
			elif cinta[c]=='X':
				c+=1
			elif cinta[c]=='b':
				estado='q2'
				c-=1
		elif estado=='q1':
			if cinta[c]=='(':
				estado='q0'
				cinta[c]='X'
				c+=1
			elif cinta[c]=='X':
				c-=1
			elif cinta[c]=='b':
				estado='q3'
				cinta[c]='0'
				c+=1
		elif estado=='q2':
			if cinta[c]=='X':
				c-=1
			elif cinta[c]=='b':
				estado='q3'
				cinta[c]='1'
				c+=1
			elif cinta[c]=='(':
				estado='q3'
				cinta[c]='0'
				c+=1
		elif estado=='q3':
			if cinta[c]=='X':
				cinta[c]='b'
				c+=1
			elif cinta[c]=='(':
				cinta[c]='b'
				c+=1
			elif cinta[c]==')':
				cinta[c]='b'
				c+=1
			elif cinta[c]=='b':
				estado='q4'
				c-=1
		elif estado=='q4':
			if cinta[c]=='1':
				estado='q5'
				c-=1
			if cinta[c]=='0':
				estado='q5'
				c-=1
			elif cinta[c]=='b':
				c-=1
		elif estado=='q5':
			if cinta[c]=='X':
				cinta[c]='b'
				c-=1
			elif cinta[c]=='(':
				cinta[c]='b'
				c-=1
			elif cinta[c]==')':
				cinta[c]='b'
				c-=1
			elif cinta[c]=='b':
				estado='q6'
				c+=1
	print borrar_blanco(cinta)	
def palindromo():
	estado='q0'
	cinta=[]
	for i in range(tamano_cinta): cinta.append('b')
	palabra=raw_input('Inserta una cadena palindrome: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado!='q8':
		if estado=='q0':
			if cinta[c]=='1':
				estado='q1'
				cinta[c]='b'
				c+=1
			elif cinta[c]=='0':
				estado='q2'
				cinta[c]='b'
				c+=1
			elif cinta[c]=='b':
				estado='q8'
				cinta[c]='1'
		elif estado=='q1':
			if cinta[c]=='1':
				estado='q3'
				c+=1
			elif cinta[c]=='0':
				estado='q3'
				c+=1
			elif cinta[c]=='b':
				estado='q8'
				cinta[c]='1'
		elif estado=='q2':
			if cinta[c]=='1':
				estado='q4'
				c+=1
			elif cinta[c]=='0':
				estado='q4'
				c+=1
			elif cinta[c]=='b':
				estado='q8'
				cinta[c]='1'
		elif estado=='q3':
			if cinta[c]=='b':
				estado='q5'
				c-=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
		elif estado=='q4':
			if cinta[c]=='b':
				estado='q6'
				c-=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='0':
				c+=1
		elif estado=='q5':
			if cinta[c]=='1':
				estado='q7'
				cinta[c]='b'
				c-=1
			elif cinta[c]=='0':
				estado='q9'
				cinta[c]='b'
				c-=1
		elif estado=='q6':
			if cinta[c]=='0':
				estado='q7'
				cinta[c]='b'
				c-=1
			elif cinta[c]=='1':
				estado='q9'
				cinta[c]='b'
				c-=1
		elif estado=='q7':
			if cinta[c]=='b':
				estado='q0'
				c+=1
			elif cinta[c]=='1':
				c-=1
			elif cinta[c]=='0':
				c-=1
		elif estado=='q9':
			if cinta[c]=='1':
				cinta[c]='b'
				c-=1
			elif cinta[c]=='0':
				cinta[c]='b'
				c-=1
			elif cinta[c]=='b':
				estado='q8'
				cinta[c]='0'
	print borrar_blanco(cinta)	

while True:
	print "\n1.- Duplicador de 1's.\n2.- Complemento binario.\n3.- Paridad.\n4.- Imagen espejo.\n5.- Verificador de parentesis anidados.\n6.- Verificador de palindromos.\n7.- Salir.\n"
	opt=input('Selecciona una opcion: ')
	if opt==1: duplicador_unos()
	elif opt==2: complemento_binario()
	elif opt==3: paridad()
	elif opt==4: espejo()
	elif opt==5: parentesis()
	elif opt==6: palindromo()
	elif opt==7: break
	else: print 'Ingresa una opcion valida.'