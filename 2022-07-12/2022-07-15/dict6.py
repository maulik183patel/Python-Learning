sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
res={}
# Keys to remove
keys = ["name", "salary"]
for i in keys:
    sample_dict.pop(i)
print(sample_dict)