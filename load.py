import json
 

# with open("myfile.json") as fh:
#     data=json.load(fh)
# print(data)


xyz=open("myfile.json","r")
x=xyz.read()
p=json.loads(x)
print(p)
