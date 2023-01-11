my_list = []

my_list.clear() # empties the list
my_list.append("Olof") # Appends the list with whatever value
my_list.append("Stenlund")
my_list.reverse() # Reverses the order
count = my_list.count("Olof") # Counts the number of times "Olof" occurs in the list
#print(count)
variable_1 = my_list.pop() # Takes the last itom from the list (removes it) and adds to variable_1
#print(variable_1)

my_list.append("Olof") 
my_list.append("Anna")
my_list.append("Börje")
my_list.sort() # Sorts alphabetically
my_list.sort(reverse=True) # Sorts in reverse
# Can define our own sorting algorithms
# Sorting mostly don't work with different data types

#print(my_list)


my_string = "Hej jag heter Ingeman"
#print(my_string)
my_string_list = list(my_string) #Creates a list of all the indexes in the variable
#print(my_string_list)

my_split_string = my_string.split('H') # Removes 'H', splits into two strings

#print(my_split_string) # Split splits the string by a certain character and creates two (or more) indexes in a list

my_email = "olof.stenlund@hotmail.com"
my_domain = my_email.split('@')[1] # splits the list by removing @ creating a hole. [1] extracs index 1 from the list
#print(my_domain)

my_address= my_email.split('@')[0] # Splits with @ and takes index 0 from the resulting list
#print(my_address)

provider = my_domain.split('.')[0] # Takes the result of my_domain ('hotmail.com') and splits by '.' creating 'hotmail' and 'com'
#print(provider) # choose index 0 ('hotmail') and save in variable provider

top_domain = my_domain.split('.')[1] # Takes the result of my_domain ('hotmail.com') and splits by '.' creating 'hotmail' and 'com'
#print(top_domain) # Choose index 1 ('com') and add to variable top_domain


my_untrimmed_string = "     Olof Stenlund    "
print(my_untrimmed_string)
my_trimmed_string = my_untrimmed_string.strip() # Strips the result from trailing spaces
print(my_trimmed_string) # Use strip() for input in the higher_lower game

letter_list = ["o", "l", "o", "f"]
my_name = "".join(letter_list) #C reates a str and performs join on that str
#print(letter_list)
print(my_name)

letter_list_2 = ["o", "l", "o", "f"]
my_name_2 = "Jag heter ".join(letter_list_2) # Joins the list elements with the text string each time.
print(my_name_2)

