Age  = 31
print(id(Age))
while Age >30:
    print("You are eligible for Entrance Exam")
    print(id(Age))
    Age += 1
    if Age == 35:
        print(id(Age))
        break