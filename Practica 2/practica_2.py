from random import choice,randint,randrange

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
def lenguaje(alf):
	np=input("Inserte el numero de palabras: ")
	l=input("Ingrese la longitud de las palabras: ")
	leng=[]
	cont=0
	while cont<np:
		pal=''
		for j in range(l):
			pal=pal+alf[randint(0,len(alf))-1]
		if pal not in leng:
			leng.append(pal)
			cont+=1
	return leng
def union(leng1,leng2):
	return leng1+leng2
def concatenar(leng1,leng2):
	conc=[[a,b]for a in leng1 for b in leng2]
	for i in range(len(conc)):
		conc[i]=''.join(conc[i])
	return conc
def resta(leng1,leng2):
	rest=[]
	for i in leng1:
		if i not in leng2:
			rest.append(i)
	return rest
def potencia(leng):
	while True:
		n=input("Ingrese la potencia: ")
		if n>-5 and n<5:
			if n>0:
				aux=leng
				for i in range(n-1):
					leng=concatenar(leng,aux)
				return n,leng
			elif n<0:
				for i in range(len(leng)):
					leng[i]=leng[i][::-1]
				aux=leng
				n=n*(-1)
				for i in range(n-1):
					leng=concatenar(leng,aux)
				return n*(-1),leng
		else:
			print "Ingrese un valor valido."
def curp():
	alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alfabetoVocales = "AEIOU"
	Year = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']
	Enditad = ['AS','BC','BS','CC','CS','CH','CL','CM','DF','DG','GT','GR','HG','JC','MC','MN','MS','NT','NL','OC','PL','QT','QR','SP','SL','SR','TC','TL','TS','VZ','YN','ZS']
	Day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
	mes = ['01','02','03','04','05','06','07','08','09','10','11','12']
	genero = ['H','M']
	for i  in range(50,100):
		Year.append(i)
	CURP = []
	for i in range(1):
		CURP.append(choice(alfabeto))
	for i in range(1,2):
		CURP.append(choice(alfabetoVocales))
	for i in range(2,4):
		CURP.append(choice(alfabeto))
	for i in range(4,5):
		Y = choice(Year)
		CURP.append(str(Y))
	for i in range(5,6):
		CURP.append(choice(mes))
	for i in range(6,7):
		CURP.append(choice(Day))
	for i in range(7,8):
		CURP.append(choice(genero))
	for i in range(8,9):
		CURP.append(choice(Enditad))
	for i in range(9,12):
		CURP.append(choice(alfabeto))
	CURP.append('0') 
	ULT = randrange(10)
	CURP.append(str(ULT))
	CURP=''.join(CURP)
	print CURP
	
print "\na)\nAlfabeto"
alf=alfabeto()
print "El alfabeto es %s." %alf
print "\nb)\nLenguaje 1"
leng1=lenguaje(alf)
print "El lenguaje 1 es %s." %leng1
print "Lenguaje 2"
leng2=lenguaje(alf)
print "El lenguaje 2 es %s." %leng2
print "\nc)\nL1+L2=%s" %union(leng1,leng2)
print "\nd)\nL1L2=%s" %concatenar(leng1,leng2)
print "\ne)\nL1-L2=%s\nL2-L1=%s" %(resta(leng1,leng2),resta(leng2,leng1))
print "\nf)"
while True:
	print "Seleccione un alfabeto\n1)L1.\n2)L2."
	n=input(">")
	if n==1: 
		pot=potencia(leng1)
		print "L1^%d=%s" %(pot[0],pot[-1])
		break
	elif n==2: 
		pot=potencia(leng2)
		print "L2^%d=%s" %(pot[0],pot[-1])
		break
	else:
		print "Seleccione una opcion valida."
print "\ng)"
curp()