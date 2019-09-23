import requests as req
import pickle

#url = "http://167.71.35.239:8080/bridge"
url = "http://algebrew.com/bridge"
def get(URL = url):
	data = req.get(URL)
	data = bytes(data.text,encoding='iso-8859-1')#data.text.encode()
	return pickle.loads(data)

def send(data, URL = url):
	serialized = pickle.dumps(data, protocol=0)
	req.post(URL, {"data":serialized},headers={'Content-Type': 'application/octet-stream'})
