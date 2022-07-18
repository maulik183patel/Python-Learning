sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
#for i in keys:
 #   for key , value in sample_dict.items():
  #      if i==key:
   #         print(key,":",value)
res=dict()
for i in keys:
    res.update({i:sample_dict[i]})
print(res)