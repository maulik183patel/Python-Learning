person = {"name": "Jessa", "country": "USA", "telephone": 1178}
#print(person.values())
#print(person["name"])
#print(person["telephone"])
#for key in person:
 #   print(key, ":" ,person[key])
#person.update({"weigth": 50})
#person["Maulik"]=78
#print(person)
#person.update({"sachin":"Australia" , "Raj":"Canada"})
#person.update([("Brijesh","Australia"),("Aj","Aus")])
person.setdefault("Maulik")
person.setdefault("name","India")
person.setdefault("state","Gujrat")
print(person)