datos = []
with open("winequality-red.csv", encoding="latin1") as fichero_csv:
# en este caso, si queremos operar con los datos, nos tenemos que fijar si existe una linea cabecera para tratarla de forma separada
	cabezera = fichero_csv.readline()
	cabezera = cabezera.strip().replace("\"","").split(";")
	for line in fichero_csv:
		# guardamos los datos en una lista de diccionarios con la pareja clave-valor
		arraylinea = line.strip().split(";") # en este caso el separador es ;
		diccionario = {}
		for posicion,elemento in enumerate(arraylinea):
			diccionario.update({cabezera[posicion]:elemento}) 
		datos.append(diccionario)
print(cabezera)
print(datos[24])
