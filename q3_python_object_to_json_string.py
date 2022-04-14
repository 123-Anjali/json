import json

n={"name":"anjali","age":20,"city":"lucknow"}
j_string=json.dumps(n)
print(j_string)
print(type(j_string))