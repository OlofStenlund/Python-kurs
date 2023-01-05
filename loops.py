# For and while loops

#while True:
 #   print("Running") # Will run forever

number = 0

while True:
    print(number)
    number = number + 1
    if number == 10:
        break

print("after loop 1")

number = 0
while number <= 10:
    print(number)
    number = number + 1

print("after loop 2") # Values that decide the loop must change, otherwise it will run forever


for i in range(10): # range starts at 0
    print(i)

for i in range(1,10): # Start at 1, end at 10 (not including)
    print(i)

for i in range(1, 10, 2): # start 1, end 10, leap 2 each time
    print(i)

my_list = ["Olof", "Stenlund", "Är", "En", "Tönt"]

for i in my_list:
    print(i)

for i in range(len(my_list)):
    print(my_list[i]) # Loops over the items in the list and prints each

for i in range(len(my_list)):
    print(i) # Prints indexes according to len()


for i, string in enumerate(my_list):
    print(i, string) # Returns indexes and their associated values


Olof = {
    "name": "Olof",
    "age": 30,
    "location": "Göteborg",
    "school": {
        "name": "EC Utbildning",
        "location": "Göteborg",
        "board": {
            "CFO": "Lasse",
            "CEO": "Maja"
        },
    },
}

for key in Olof.keys():
    print(key)

for values in Olof.values():
        print(values)

for key, values in Olof.items():
    print(key, values)