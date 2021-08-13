
import sys
try:
    Val1 = int(input("Enter First No"))
    Val2 = int(input("Enter Second No"))

    print(Val1//Val2)
    print(Name)

except ZeroDivisionError:
    print("You cant Divide a No by 0 - ZERO")
    error = sys.exc_info()[0]
    print(error)
except Exception :
    error  = sys.exc_info()[0]
    print("Handling all Exception from Global Exception Class ")


finally:
    print("Thank you for using our Exceptional handling Demo ")