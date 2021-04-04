from flask import Flask
import requests
app = Flask(__name__)

@app.route('/id/<valor>')
def profile(valor):
	r = requests.get('http://api.citybik.es/v2/networks/bicing')
	bicingJson = r.json()
	for station in bicingJson['network']['stations']:
		if station['id'] == valor:
			selected_station = station
			break
	return selected_station
