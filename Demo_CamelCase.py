
import camelcase

c = camelcase.CamelCase()
MyMessage = "i am learning Python"
#print(MyMessage)
print(c.hump(MyMessage))