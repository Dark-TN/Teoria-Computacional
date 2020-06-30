global tamano_cinta
tamano_cinta=100

def borrar_blanco(cinta):
	cadena=[]
	for i in cinta: 
		if i != 'b': cadena.append(i)
	return ''.join(cadena)
def reverso():
	estado='q0'
	cinta=[]
	for i in range(tamano_cinta): cinta.append('b')
	palabra=raw_input('Inserta una cadena binaria: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado!='q9':
		if estado=='q0':
			if cinta[c]=='0':
				c-=1
			elif cinta[c]=='1':
				c-=1
			elif cinta[c]=='b':
				estado='q1'
				cinta[c]='A'
				c+=1
		elif estado=='q1':
			if cinta[c]=='0':
				c+=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='b':
				estado='q2'
				cinta[c]='Z'
				c-=1
		elif estado=='q2':
			if cinta[c]=='0':
				estado='q6'
				cinta[c]='b'
				c+=1
			elif cinta[c]=='1':
				estado='q3'
				cinta[c]='b'
				c+=1
			elif cinta[c]=='b':
				c-=1
			elif cinta[c]=='A':
				estado='q8'
				cinta[c]='b'
				c-=1
		elif estado=='q3':
			if cinta[c]=='b':
				c+=1
			elif cinta[c]=='Z':
				estado='q4'
				c+=1
		elif estado=='q4':
			if cinta[c]=='0':
				c+=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='b':
				estado='q5'
				cinta[c]='1'
				c-=1
		elif estado=='q5':
			if cinta[c]=='0':
				c-=1
			elif cinta[c]=='1':
				c-=1
			elif cinta[c]=='Z':
				estado='q2'
				c-=1
		elif estado=='q6':
			if cinta[c]=='b':
				c+=1
			elif cinta[c]=='Z':
				estado='q7'
				c+=1
		elif estado=='q7':
			if cinta[c]=='0':
				c+=1
			elif cinta[c]=='1':
				c+=1
			elif cinta[c]=='b':
				estado='q5'
				cinta[c]='0'
				c-=1
		elif estado=='q8':
			if cinta[c]=='b':
				c+=1
			elif cinta[c]=='Z':
				estado='q9'
				cinta[c]='b'
				c+=1
	print borrar_blanco(cinta)
def consecutivo_binario():
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
				c+=1
			elif cinta[c]=='b':
				estado='q1'
				c-=1
		elif estado=='q1':
			if cinta[c]=='0':
				estado='q2'
				cinta[c]='1'
				c-=1
			elif cinta[c]=='1':
				cinta[c]='0'
				c-=1
			elif cinta[c]=='b':
				estado='q2'
				cinta[c]='1'
				c-=1
	print borrar_blanco(cinta)
	
consecutivo_binario()
print "\n1.- Cadena invertida.\n2.- Numero consecutivo binario.\n3.- Salir.\n"
	opt=input('Selecciona una opcion: ')
	if opt==1: reverso()
	elif opt==2: consecutivo_binario()
	elif opt==3: break
	else: print 'Ingresa una opcion valida.'