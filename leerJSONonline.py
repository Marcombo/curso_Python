import json
import requests
url = "https://opendata-ajuntament.barcelona.cat/data/api/3/action/package_search"
resp = requests.get(url)
print(resp)
#print(resp.content)
jcontent = json.loads(resp.content)
for element in jcontent["result"]["results"]:
	print (element["code"])
#print(jcontent["result"]["results"])
