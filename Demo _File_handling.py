def MYFileDisplay():
    myFile1 = open("Mydetails.txt",'r')
    Output = myFile1.readlines()
    print(Output)

Myfile = open("Mydetails.txt",'a')
message = "You can follow me on  twitter also "
Myfile.write(message)

MYFileDisplay()