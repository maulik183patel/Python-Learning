sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
res={}

for i in keys:
    res.update({i:sample_dict[i]})
print(res)