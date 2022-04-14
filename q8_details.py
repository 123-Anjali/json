import json 
keys1=["name","designation","age","salary"]
a=["neelam","programer","24","24000",]
emp1={}
emp2={}
emp3={}
emp4={}
dict={}
for i in range (len(keys1)):
    emp1[keys1[i]]=a[i]
    dict["employees1"]=emp1
    keys2=["name","designation","age","salary"]
    b=["komal","trainer","24","20000"]
    for j in range (len(keys2)):
        emp2[keys2[j]]=b[j]
        dict["employees2"]=emp2
        keys3=["name","designation","age","salary"]
        c=["abhishek","CEO","29","5000000"]
        for x in range (len(keys3)):
            emp3[keys3[x]]=c[x]
            dict["employees"]=emp3
            keys4=["name","designation","age","salary"]
            d=["anuradh","HR","25","25000"]
            for y in range(len(keys4)):
                emp4[keys4[y]]=d=[y]
                dict["employees"]=emp4
out_file=open("myfile.json","w")
json.dump(dict,out_file,indent=6)
out_file.close()

