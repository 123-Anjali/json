import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": 34,
        "salary": 54000
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainer",
        "age": 24,
        "salary": 40000
    },
}
file=open("myfile.json","w")
json.dump(dict1,file,indent=4)




# # a=(-18//4)
# # print(a)

# # a=2**3**2
# # print(a)





