test_list = [1, 4, 5, 6, 3, 5]

# printing original list
print ("The original list is : " + str(test_list))

# First naive method
# using loop method to print last element
for i in range(len(test_list)):

    if i == (len(test_list)-1):
        print("The last element of list using loop : ",test_list[i])

