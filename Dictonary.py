# Dictonary contains key-value pair.

d1 = {}
print(type(d1))

d2 = {"Ritesh":"eggs",
      "Rahul":"burger",
      "Tony":"bear"}
print(d2)
print(d2["Ritesh"])

d2["jenny"] = "cute"
print(d2)

d2["speaker"] = "mivi"
print(d2)
del d2["speaker"]
print(d2)

d2[258] = "waste"
print(d2)
del d2[258]
print(d2)

d3 = d2.copy()
del d3["Ritesh"]
print(d3)
print(d2)

d2.update({"veer":"zara"})
print(d2)

print(d2.keys())
print(d2.items())

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)