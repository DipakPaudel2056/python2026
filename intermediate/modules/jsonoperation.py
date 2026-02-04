# we can also work with json data in python
import json
from tkinter.messagebox import IGNORE
data = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(data)
print("Name:", parsed_data["name"]) 
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])
json_string = json.dumps(parsed_data)
print("JSON String:", json_string)
