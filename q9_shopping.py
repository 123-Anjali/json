import json
d={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20"}}
with open("tat.json_list","w") as f:
    data=json.dump(d,f,indent=4)
print(data) 
item=(input("kaun sa item kharidna hai"))
quantity=int(input("tum kitne item kharidna chahte ho"))
with open ("tat.json_list") as f:
    data=json.load(f)
    for x,y in data .items():
        if item in y:
            for a,b in y.items():
                if item==a:
                    if  (quantity)<=int(b):
                       b1=int(b)-quantity
                       y[a]=b1
                    else:
                       d=quantity-int(b)
                       y[a]=d
        else:
            y[item]=str(quantity)
            print(data)
with open ("tat.json_list","w") as f:
    json.dump(data,f,indent=4)
        

