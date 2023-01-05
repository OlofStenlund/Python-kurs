# Lists

# Can contain different types of elements

list1 = [] # Square brackets to contain the list
list2 = list() # Use to add items to list?
list3 = [1, 2, 3, 4, 5]
list4 = list(["hej", "Då", 5, True]) # We'll get to this later

listoflists1 = [list3, list4] 
listoflists2 = [[1,2,3], [4,5,6], [7,8,9]]

print(listoflists1)
print(listoflists2)

print(list4[0]) # Prints the first item (number 0) in the list
greeting = (list4[0]) # make a variable out of the result
print(greeting)

print(len(list3)) # Number of elements in the list
print(type(len(list3)))

# get the last index: len-1
list_len = len(list3)
print(list_len) # prints last item in the list
print(list3[list_len-1]) # prints last item in the list
print(list4[-1]) # prints last item in the list

# If you make listn = listx, a change to either will change both.

list1 = list2.copy() #creates a copy (list1 is the copy)
