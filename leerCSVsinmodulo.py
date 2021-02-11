datos = []
with open("winequality-red.csv", encoding="latin1") as fichero_csv:
# en este caso, si queremos operar con los datos, nos tenemos que fijar si existe una linea cabecera para tratarla de forma separada
	cabecera = fichero_csv.readline()
	for line in fichero_csv:
		# guardamos los datos en una lista bidimensional
		arraylinea = line.strip().split(";") # en este caso el separador es ;
		datos.append(arraylinea)
print(cabecera)
print(datos)
