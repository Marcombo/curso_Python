import csv
datos = []
with open("winequality-red.csv", encoding="latin1") as fichero_csv:
	lector = csv.reader(fichero_csv,delimiter=";")
	next(lector,None) # nos saltamos la cabezera
	for line in lector:
		# no tenemos que hacer el split, ya que en este caso line ya es un vector y no un string
		# guardamos los datos en una lista bidimensional
		datos.append(line)
print(datos)
