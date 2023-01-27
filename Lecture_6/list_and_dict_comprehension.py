# [x for x in iterable] is a way to create a list

#------List comprehension----------

# A list of dictionaries
people = [{"name": "Olof", "age": 33},
        {"name": "Aaron", "age": 25},
        {"name": "Alice", "age": 38},
        {"name": "Joar", "age": 12} ]

print(people)

# Create a list with all the names from people
# [x for x in iterable] -> x is the variable we create right here.
# We want just the "name" from each instance of x in people
# For each x in people, we want x["name"]
names = [person["name"] for person in people]
ages = [person["age"] for person in people]
print(names, ages)


#------Dict comprehension---------

# Creates something something key values bla bla
# Names as keys and ages as values
my_people = {person["name"]: person["age"] for person in people}
print(my_people)

# letters = [letter for name in names in names for letter in name]