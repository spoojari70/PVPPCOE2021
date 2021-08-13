num1 = int(input("Enter First No"))
num2 = int(input("Enter Second No"))
try:
    Value  = num1/num2
    print(Value)
except:
    print("You can't divide a no by Zero.. Not possible on earth  ")

finally:
    print("This application works perfectly fine with a non Zero Value ")
