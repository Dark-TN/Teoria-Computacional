from itertools import combinations

def rango():
	while True:
		c=raw_input('Inserta el rango separado por un guion medio (a-z): ')
		alf=[]
		'-'.split(c)
		for i in range(ord(c[0]),ord(c[-1])+1):
			alf.append(chr(i))
		if len(alf) < 3: 
			print "Error. Inserta el alfabeto nuevamente."
		else:
			return alf
def individual():
	while True:
		c=raw_input('Inserta el alfabeto separando los elementos por una coma (a,b,c,...): ')
		alf=[]
		','.split(c)
		for i in c:
			if i != ',': alf.append(i)
		if len(alf) < 3: 
			print "Error. Inserta el alfabeto nuevamente."
		else:
			return alf
def alfabeto():
	while True:
		print "Elija una opcion:\n1.- Insertar alfabeto por rango.\n2.- Insertar alfabeto individualmete."
		opt=input(">")
		if opt==1: 
			return rango()
		elif opt==2: 
			return individual()
		else: print "Error. Elija una opcion valida."
def cadena(alf):
	while True:
		cont=0
		c=raw_input('Inserte la cadena: ')
		for i in c:
			if i in alf:
				cont+=1
		if cont==len(c):
			return c
		else: 
			print "Error. Inserte la cadena nuevamente."
def potencia(cad):
		aux=cad
		pot=input('Inserte la potencia: ')
		if pot>0:
			for i in range(pot-1):
				cad=cad+aux
			return pot,cad
		elif pot==0: 
			return 0,"Cadena vacia."
		else:
			cad=cad[::-1]
			aux=cad
			pot=pot*(-1)
			for i in range(pot-1):
				cad=cad+aux
			return pot*-1,cad
def ocurrencia(cad):
	c=raw_input("Ingresa el caracter a buscar: ")
	cont=0
	for i in cad:
		if i == c: 
			cont+=1
	return c,cont
def prefijo_sufijo(cad1,cad2):
	ind=cad2.find(cad1)
	if ind >= 0:
		if cad1==cad2[:ind]:
			if cad1==cad2:
				print "%s es prefijo de %s." %(cad1,cad2)
			else:
				print "%s es prefijo propio de %s." %(cad1,cad2)
		elif cad1==cad2[ind:]:
			if cad1==cad2:
				print "%s es sufijo de %." %(cad1,cad2)
			else:
				print "%s es sufijo propio de %s." %(cad1,cad2)
		else:
			if cad1==cad2:
				print "%s es subcadena de %s." %(cad1,cad2)
			else:
				print "%s es subcadena propia de %s." %(cad1,cad2)
	else:
		if cad1==' ':
			print 'La cadena vacia es prefijo,sufijo y subcadena de %s.' %cad2
		else:
			print '%s no es prefijo,sufijo ni subcadena de %s.' %(cad1,cad2)
def potencia_alfabeto(alf,n):
	pow=[]
	for i in combinations(alf,n):
		pow.append(list(i))
	return pow
def combinacion(combinar, lista):
	new_comb=[[a,b]for a in combinar for b in lista]
	return new_comb 		
def combinacion_2(combinar,lista):
	new_comb=[]
	for i in combinar:
		new_comb+=[[a,b,c]for a in i for b in i for c in lista]
	return new_comb
print "\na)\nAlfabeto 1"
alf1=alfabeto()
print "El alfabeto 1 es %s." %alf1
print "\nb)\nAlfabeto 2"
alf2=alfabeto()
print "El alfabeto 2 es %s." %alf2
print "\nc)\nCadena 1"
c1=cadena(alf1)
print "La cadena 1 es %s." %c1
print "Cadena 2"
c2=cadena(alf1)	
print "La cadena 2 es %s." %c2
print "\nd)"
p=potencia(c1+c2)
print "(%s%s)^%d=%s" %(c1,c2,p[0],p[-1])
print "\ne)"
oc=ocurrencia(c1)
print "|%s|%s=%d" %(c1,oc[0],oc[-1])
print "\nf)"
prefijo_sufijo(c1,c2)
print "\ng)"
n=input("Inserte la potencia a la cual quiere elevar el alfabeto 1: ")
print "A1^%d=" %n,potencia_alfabeto(alf1,n)
n=input("Inserte la potencia a la cual quiere elevar el alfabeto 2: ")
print "A2^%d=" %n,potencia_alfabeto(alf2,n)
print "\nh)"
comb=combinacion(alf1,alf2)
print "A1*A2=",comb
print "\ni)"
print "A1*A2*A1=",combinacion_2(comb,alf1)