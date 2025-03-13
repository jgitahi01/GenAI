#dictionary with personal information
my_info = {"name": "John", "age": 30, "city": "New York"}
#adding a new key value 
my_info["favortite_color"] = "blue"
#updationg the city key to a new city
my_info["city"] = "San Francisco"
#printing all key values 
for key, value in my_info.items():
    print(f"{key}: {value}")
    