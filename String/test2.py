s = input(" Type your string and Press Enter key:=")

while s.upper() != "END" and s.lower != "Bye" and s.upper != "EOF":


    for c in s:
        print("\n", ord(c), "is The ASCII code of", c)

    if c.isupper():
        print("==>", c, "is a upper case letter. ")
    elif c.islower():
        print("==>", c, "is a lower case letter. ")
    elif c.isspace():
        print(c,"==>is a space. ")
    else:
        print("END")