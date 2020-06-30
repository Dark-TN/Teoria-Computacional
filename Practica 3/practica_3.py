def afd_1():
	digitos = {'0','1','2','3','4','5','6','7','8','9'}
	estados = {4,7}
	cadena = raw_input("Ingresa cadena: ")
	estado = 1
	for i in cadena:
		if estado == 1:
			if i in digitos:
				estado = 2
			else:
				estado = 0
				break
		elif estado == 2:
			if i in digitos:
				estado = 2
			elif i == ".":
				estado = 3
			elif i == "E":
				estado = 5
			else:
				estado = 0
				break
		elif estado == 3:
			if i in digitos:
				estado = 4
			else:
				estado = 0
				break
		elif estado == 4:
			if i in digitos:
				estado = 4
			elif i == "E":
				estado = 5
			else:
				estado = 0
				break
		elif estado == 5:
			if i in digitos:
				estado = 7
			elif i == "-" or i == "+":
				estado = 6
			else:
				estado = 0
				break
		elif estado == 6:
			if i in digitos:
				estado = 7
			else:
				estado = 0
				break
		elif estado == 7:
			if i in digitos:
				estado = 7
			else:
				estado = 0
				break
	if estado in estados:
		print "Aceptada"
	else:
		print "No aceptada"
def afd_2():
	estados = {0,4}
	cadena = raw_input("Ingrese cadena: ")
	estado = 0
	for i in cadena:
		if estado == 0:
			if i == '0':
				estado = 1
			elif i == '1':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 1:
			if i == '0':
				estado = 0
			elif i == '1':
				estado = 2
			else:
				estado = -1
				break
		elif estado == 2:
			if i == '0':
				estado = 0
			elif i == '1':
				estado = 3
			else:
				estado = -1
				break
		elif estado == 3:
			if i == '0' or i == '1':
				estado = 3
			else:
				estado = -1
				break
		elif estado == 4:
			if i == '0':
				estado = 1
			elif i == '1':
				estado = 5
			else:
				estado = -1
				break
		elif estado == 5:
			if i == '0' or i == '1':
				estado = 5
			else:
				estado = -1
				break
	if estado in estados:
		print "Aceptada"
	else:
		print "No aceptada"
def afd_3():
	estados = {4}
	cadena = raw_input("Ingrese cadena: ")
	estado = 0
	for i in cadena:
		if estado == 0:
			if i == 'a':
				estado = 1
			elif i == 'b':
				estado = 7
			elif i == 'c':
				estado = 11
			else:
				estado = -1
				break
		elif estado == 1:
			if i == 'a':
				estado = 2
			elif i == 'b':
				estado = 3
			elif i == 'c':
				estado = 5
			else:
				estado = -1
				break
		elif estado == 2:
			if i == 'a' or i == 'b' or i == 'c':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 3:
			if i == 'b':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 4:
			if i == 'a' or i == 'b' or i == 'c':
				estado = 6
			else:
				estado = -1
				break
		elif estado == 5:
			if i == 'c':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 6:
			if i == 'a' or i == 'b' or i == 'c':
				estado = 6
			else:
				estado = -1
				break
		elif estado == 7:
			if i == 'a':
				estado = 9
			elif i == 'b':
				estado = 8
			elif i == 'c':
				estado = 10
			else:
				estado = -1
				break
		elif estado == 8:
			if i == 'a' or i == 'b' or i == 'c':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 9:
			if i == 'a':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 10:
			if i == 'c':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 11:
			if i == 'a':
				estado = 13
			elif i == 'b':
				estado = 14
			elif i == 'c':
				estado = 12
			else:
				estado = -1
				break
		elif estado == 12:
			if i == 'a' or i == 'b' or i == 'c':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 13:
			if i == 'a':
				estado = 4
			else:
				estado = -1
				break
		elif estado == 14:
			if i == 'b':
				estado = 4
			else:
				estado = -1
				break
	if estado in estados:
		print "Aceptada"
	else:
		print "No aceptada"
def afd_4():
	digitos = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
	'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
	estados = {6}
	cadena = raw_input("Ingrese un correo electronico: ")
	estado = 0
	for i in cadena:
		if estado==0:
			if i in digitos:
				estado=1
			else:
				estado = -1
				break
		elif estado==1:
			if i in digitos:
				estado=1
			elif i=='.':
				estado=2
			elif i=='@':
				estado=3
			else:
				estado = -1
				break
		elif estado==2:
			if i in digitos:
				estado=2
			elif i=='.':
				estado=1
			elif i=='@':
				estado=3
			else:
				estado = -1
				break
		elif estado==3:
			if i in digitos:
				estado=4
			else:
				estado = -1
				break
		elif estado==4:
			if i in digitos:
				estado=4
			elif i=='.':
				estado=5
			else:
				estado = -1
				break
		elif estado==5:
			if i in digitos:
				estado=6
			else:
				estado = -1
				break
		elif estado==6:
			if i in digitos:
				estado=6
			else:
				estado = -1
				break
	if estado in estados:
		print "Correo aceptado"
	else:
		print "Correo no aceptado"
					
print "\na)"
afd_1()
print "\nc)"
afd_2()
print "\nd)"
afd_3()
print "\nd)"
afd_4()