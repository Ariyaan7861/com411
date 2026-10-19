print ("Program Started!")
char= input("Please enter a standard character")


length= len(char)
if length==1:
    ascii= ord(char)
    print (f"The ASCII code for {char} is {ascii}.")
else:
    print ("Please enter 1 character")
