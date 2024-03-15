import json 

data ={"name":kim,  "age":23}

print(data["name"], type(data), type(json.dumps(data)))
res_data = json.dumps(data)
print(type(json.loads(res_data)))