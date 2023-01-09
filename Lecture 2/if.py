# Logik

# == (equal to), !=(not equal to), >(smaller than), 
# <(greater than), >= (smaller than or equal to), <= (greater than or equal to)
# and, not, or
# "=" is an assignment operator, "==" is a comparison operator

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

truth = Olof["name"]
print(truth, type(truth)) # Returns name, str

truth = 1 + 1 == 2
print(truth, type(truth)) # Returns "True", bool 

truth = Olof["age"] > 25
print(truth) # Returns true, because age (30) is greater than 25

truth = Olof["age"] != 30
print(truth) # Returns false, because age (30) is in fact equal to 30

truth = Olof["age"] == 30 and Olof["name"] == "Olof"
print(truth) # Prints true
truth = Olof["age"] == 25 or Olof["name"] == "Olof"
print(truth) # Prints True
truth = Olof["age"] == 25 and Olof["name"] == "Olof"
print(truth) # Prints False
truth = Olof["age"] == 30 and not Olof["name"] == "Olof"
print(truth) # Prints false, because name == Olof

# Will always run
if True:
    print("It's damn true!")

# Will never run
if False:
    print("It's false")

if Olof["age"] >= 30:
    print("Old AF")

if not Olof["age"] >= 30:
    print("youngling")


if Olof["age"] < 30:
    print("youngling") # If age less than 30
elif Olof["age"] == 36:
    print("yo 36") # I age == 36
elif Olof["age"] > 30:
    print("You old AF") # If age is over 30
else: # If none of the above statements are true
    print("How old are ya?") # Only runs is age == 30


# Värden in datatyper kan evalueras i if-satser

a_zero = 0
a_one = 1
neg_one = -1

if a_zero:
    print("zero") # Will not run, since the value 0 is converted to False
if a_one:
    print("one") # Will run, 1 is True

if a_zero == 0:
    print("zero") # Will run, since if-statement returns True

if neg_one:
    print("-1") # Will run, negative numbers return True