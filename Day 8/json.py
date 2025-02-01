import json

data={"name": "Vaish", "age": 21,"city": "Hyderabad"}
json_data= json.dumps(data)
print(f"JSON data:",{json_data})

parsed_data= json.loads(json_data)
print(f"Parsed data: {parsed_data}")

with open("data.json", "w") as file:
    json.dump(data,file)