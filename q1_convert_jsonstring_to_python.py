import json
x='{"name":"anjali","age":20,"city":"lucknow"}'
y=json.loads(x)
print(y)
print(type(y))