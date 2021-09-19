#List of character before delete the last position
Character_list = []
#List of character after delete the last position
Character_list_no_last = []
#Get the word or string from the user
Character = str(input("\nType your word or string and Press Enter key:= "))
#Contain the word or string in "Character_list[]"
Character_list.append(Character)
#Make the condition if you type END,BYE,EOF the program will stop to receive a new word or string
while Character != "END" and Character != "BYE" and Character != "EOF":
    for c in Character:
        #Display an ASCII value of each character
        print("===>", ord(c), "is The ASCII code of", "(", c, ")")
        #Display a upper case character
        if c.isupper() == True:
            print("--->", "(", c, ")", "is a upper case letter.")
        #Display a lower case character
        elif c.islower() == True:
            print("--->", "(", c, ")", "is a lower case letter.")
        #Display a number
        elif c.isalnum() == True:
            print("--->", "(", c, ")", "is a number.")
        #Display a space
        elif c.isspace() == True:
            print("     (", c, ")", "is a space.")
    #Get the word or string from the user and compare in "while loop"
    #you type END,BYE,EOF the program will stop to receive a new word or string
    print("\n**To end the file type ( END,BYE,EOF) or continue..**")
    Character = input("Type your word or string and Press Enter key:= ")
    # Contain the word or string in "Character_list[]"
    Character_list.append(Character)
#Display all words or string you type
print("\n==Your words are below==")
#It will display all character but not the last[-1] position character the will reserve for (END,BYE,EOF)
for i in range(len(Character_list)-1):
    print("Line", i+1, end=". ")
    print(Character_list[i])
#It will make new list which will not contain the last position (END,BYE,EOF) in "Character_list_no_last"
for i in range(len(Character_list)-1):
    new = Character_list[i]
    Character_list_no_last.append(new)
#After getting the new list we will join all character in the "Character_list_no_last"
#into the new list with will set each characters into any position in "Character_join_list"
Character_join_list = ""
Character_join_list = Character_join_list.join(Character_list_no_last)
#Display total characters from "Character_join_list"
char = len(Character_join_list)
print("\nYour total characters(included space) of word is := ", char)
#Display total lines from "Character_join_list"
line = len(Character_list)
print("Your total lines of word is:= ", line-1)
#Display total number of letter from  "Character_join_list"
letter = sum(c.isalpha() for c in Character_join_list)
print("Your total counts of letter is :=", letter)
#Display total number of only Upper case letter from "Character_join_list"
letter_up = sum(c.isupper() for c in Character_join_list)
print("Your total counts of upper case letter is:=", letter_up)
#Display total number of only Lower case letter from "Character_join_list"
letter_lower = sum(c.islower() for c in Character_join_list)
print("Your total counts of lower case letter is:=", letter_lower)
#Display counts of number from "Character_join_list"
number = sum(c.isdigit() for c in Character_join_list)
print("Your total counts of number is :=", number)
#display counts of Empty space from "Character_join_list"
space = sum(c.isspace() for c in Character_join_list)
print("Your total counts of empty space is :=", space)
#Display the most frequency character from "Character_join_list"
from collections import Counter
res = Counter(Character_join_list)
res = max(res, key=res.get)
print("Your most frequency character is:= " + str(res))
#Display frequency of each character
res = {i: Character_join_list.count(i) for i in set(Character_join_list)}
print("Your frequency of each characters:=\n" + str(res))
print("\n******End of processing*****")
