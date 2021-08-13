Mercedez = {"Color" : "Black",
            "Engine Type": "6 Cylinder",
            "Model" : "E-Class"}

print(Mercedez["Color"])
Mercedez["Color"] = "RED"
print(Mercedez["Color"])
print(len(Mercedez))

print(Mercedez.keys())
print(Mercedez.values())

for key in Mercedez:
    print(key)