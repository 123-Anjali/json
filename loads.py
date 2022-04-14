import json


#some json:
x='{"name":"anjali","age":20,"city":"new Yark"}'
#parse x:
y=json.loads(x)
#the result is a python dictionary:
print(y)
print(type(y))

