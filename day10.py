#List containing 5 cities
city = ["Milano", "Atena", "Paris", "Londra", "Caen"]

#Display first city in the list
print(city[0])

#Display last city in the list
print(city[4])

#Display length of the list
print(len(city))

#List containing animals
animals = ["cat", "dog", "rat"]

#Add parrot to the animals list
animals.append("parrot")

#Delete rat from the animals list
animals.remove("rat")

#Display the animals list
print(animals)

#Dictionary
car = {
    "brand": "Audi",
    "model": "A4",
    "year": 2015
}

#Add color parameter
car["color"] = "Red"
#Change the value of year parameter
car["year"] = 2020
#Display the updated dictionary
print(car)

#Dictionary no2
user = {
    "id": 15,
    "username": "admin",
    "email": "admin@test.com",
    "active": True
}

#Display user name
print(user["username"])
#Dispaly email
print(user["email"])
#Display if user is active
print(user["active"])

#List of Dictionaries no3
product = [
    {"name":"Laptop", "price":3000},
    {"name":"Phone", "price":1500},
    {"name":"Mouse", "price":50}
]

print(product[0])
