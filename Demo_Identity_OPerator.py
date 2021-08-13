"""
Identity OPerator Implemetnation

"""


Cars = [ "Ferrari", "Hummer", "Ashton Martin"]
DreamCars = ["Tesla", "Porsche","Rolls Royce"]

MyFriendCars  = DreamCars

if Cars == DreamCars :
    print("Collections are Same")
else :
    print("Collections are different")

print( Cars is DreamCars)

print(DreamCars is MyFriendCars)

print( "Tesla" in Cars)