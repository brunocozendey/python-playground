import requests

def consulta():
	response = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
	print(response.status_code)
	print(response.json())
	for arg in response.json():
		print(arg)

consulta()	
