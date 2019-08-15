import requests as req
import pickle

def get(URL = "http://167.71.35.239:8080/bridge"):
	data = req.get(URL)
	print(len(data.text))
	data = bytes(data.text,encoding='iso-8859-1')#data.text.encode()
	print(len(data))
	return pickle.loads(data)

def send(data, URL = "http://167.71.35.239:8080/bridge"):
	serialized = pickle.dumps(data, protocol=0)
	#print(serialized)
	req.post(URL, {"data":serialized},headers={'Content-Type': 'application/octet-stream'})
