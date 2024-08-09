opelObj = {
    "brand": "Opel",
    "model": "Corsa",
    "year": 2020
}

result = opelObj["brand"]
result = opelObj.get("brand")

# for x in opelObj:
#     print(x)

# for x in opelObj:
#     print(opelObj[x])

# for x in opelObj.values():
#     print(x)

# for x, y in opelObj.items():
#     print(x, y)

# result = "brand" in opelObj
# result = len(opelObj)
# opelObj["color"] = "red"
# opelObj.pop("color")
# opelObj.popitem()

# del opelObj["brand"]
# del opelObj
# opelObj.clear()

obj = opelObj.copy()  # reference

obj["brand"] = "Mazda"

opelObj.update({
    "brand": "Bmw",
    "color": "Red"
})

# print(result)
print(obj)
print(opelObj)
