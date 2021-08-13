#name  = input("Enter your name\n")

try:
    print(name)

except:
    print("You can not call a variable without initilizing it ")

finally:
    Email = input("Your name is valid, enter your Email ID ")
    print("Your Email ID is "+Email)
    print("Thank you for using our application ")