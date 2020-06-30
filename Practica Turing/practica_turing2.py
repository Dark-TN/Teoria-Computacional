global tamano_cinta
tamano_cinta=100

def borrar_blanco(cinta,blanco):
	cadena=[]
	for i in cinta: 
		if i != blanco: cadena.append(i)
	return ''.join(cadena)
def maquina_turing():
	alf_c=raw_input('Inserte el alfabeto de la cinta: ')
	alf_c=alf_c.split(',')
	alf=raw_input('Inserte el alfabeto de entrada: ')
	alf=alf.split(',')
	blanco=raw_input('Inserte el caracter blanco: ')
	if blanco not in alf_c:
		print 'Error: El caracter blanco no pertenece al alfabeto de la cinta.'
		return
	if blanco in alf:
		print 'Error: El caracter blanco pertenece al alfabeto de entrada.'
		return
	estados=raw_input('Inserte los estados: ')
	estados=estados.split(',')
	estado=raw_input('Inserta el estado inicial: ')
	if estado not in estados:
		print 'Error: El estado inicial no pertenece al conjunto de estados.'
		return
	estados_f=raw_input('Inserta los estados finales: ')
	estados_f=estados_f.split(',')
	for i in estados_f:
		if i not in estados:
			print 'Error: El estado final no pertenece al conjunto de estados.'
			return
	transiciones=[]
	print 'Inserte la tabla de transicion: '
	for i in estados:
		for j in alf_c:
			transicion=[[i,j]]
			t=raw_input('%s,%s: ' %(i,j))
			t=t.split(',')
			transicion.append(t)
			transiciones.append(transicion)
	cinta=[]
	for i in range(tamano_cinta): cinta.append(blanco)
	palabra=raw_input('Inserta una cadena: ')
	c=m=(tamano_cinta-len(palabra))/2
	for i in palabra:
		cinta[m]=i
		m+=1
	while estado not in estados_f:
		q=[estado,cinta[c]]
		for i in transiciones:
			if i[0]==q:
				if len(i[-1]) == 3:
					estado=i[-1][0]
					cinta[c]=i[-1][1]
					if i[-1][-1]=='D': c+=1
					elif i[-1][-1]=='I': c-=1
	print 'Salida:',borrar_blanco(cinta,blanco)
	
maquina_turing()
	