# Text.txt:-
# Name Abhishek
# Designation CEO of navgurukul
#  Gender male
# Age 29

xyz=open("st.txt","w")
for i in range(5):
    name=input("enter the name=")
    xyz.write(name)
    xyz.write("\n")
xyz.close()



import json
filename="st.txt"
dict1={}
with open (filename) as fh:
    for line in fh:
        command,descrtption=line.strip().split(None,1)
        dict1[command]=descrtption.strip()
out_file=open("txt.json","w")
json.dump(dict1,out_file,indent=4,sort_keys=False)
out_file.close()