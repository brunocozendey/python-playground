from zeep import Client

client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method(bstrParam1='oi', bstrParam2='tchau')
print(result)
