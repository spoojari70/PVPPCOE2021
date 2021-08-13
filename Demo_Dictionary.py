MySportsCar = {"color":"Red",
"Model":"Bugatti-veyron",
"Engine":"Hybrid" }
def Display():
    print(MySportsCar)
    for cars in MySportsCar.values():
        print(cars)

#Changing element
MySportsCar["color"] = "Black"
Display()
MySportsCar["Suspension"] = "Hybrid"
Display()
MySportsCar["color"]= "Yellow"
Display()