
#Tuple Implemetaation with the help of Constructor
Series = tuple(("Mr Robot","DarkWeb","Snowden"))
print(Series)

"""
[] = Square - LIST
() = Round - Tuple 
{} = Curly - Set and Dictionary{K,V}
<> = Angular - 

"""

Netflix_WatchList = ("Money Heist" ,"Breaking Bad" ,"Prision Break","Breaking Bad")

def Display():
    for i in range(3):
        print(Netflix_WatchList[i])
#Netflix_WatchList[2] = "13 reason Why "

print(Netflix_WatchList.count("Breaking Bad"))
print(len(Netflix_WatchList))

Display()