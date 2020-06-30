from re import compile,DOTALL

def comentarios(archivo):
	arc=open(archivo,'r')
	codigo=arc.read()
	ex = compile(r"/\*", DOTALL)
	if len(ex.findall(codigo))==0:
		print "No hay comentarios en el codigo fuente"
	else:
		ex = compile(r'/[^/]*/', DOTALL) 
		if len(ex.findall(codigo))==0:
			print "Uso incorrecto de comentarios."
		else:
			print "Uso correcto de comentarios."
def funciones_variables(archivo):
	arc=open(archivo,'r')
	codigo=arc.read()
	ex = compile(r"int|char|float|void|boolean", DOTALL)
	if len(ex.findall(codigo))==0:
		print "No se encontraron nombres de variables ni funciones en el codigo fuente."
	else:
		ex = compile(r"[a-zA-Z_][a-zA-Z0-9_]{0,31};|[a-zA-Z_][a-zA-Z0-9_]{0,31}\( ", DOTALL)
		print ex.findall(codigo)
		if len(ex.findall(codigo))==0:
			print "Uso incorrecto de funciones y variables."
		
funciones_variables('c.c')