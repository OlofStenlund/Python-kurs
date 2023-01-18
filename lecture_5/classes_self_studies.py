        
# -----------------Private and public attributes-----------------------

class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

olof = Person("Olof", 33)

# We can hide attributes 
# Then we must use getters and setters to get or set these attributes

# Public attribute
print(olof.name)

olof.name = "Evert"
# Oops, now a new value was assigned easily
print(olof.name)

# We can make the attributes private

class SpyName:
    def __init__(self, name: str, age: int, spyname: str):
        self.name = name
        self.age = age
        self.__spyname = spyname

hanna = SpyName("Hanna", 33, "bajskorv") # Spyname can be assigned??
print(hanna.name) # Cannot print spyname

# We can create a getter in the function to be able to get it.

class SpyName2:

    def __init__(self, name: str, age: int, spyname: str):
        self.name = name
        self.age = age
        self.__spyname = spyname

    def get_spy_name(self):
        print(self.__spyname)
        return self.__spyname

    def set_spy_name(self, spyname: str):
        self.__spyname = spyname
    
    def __reveal_spyname(self): # Private fucntion
        print(self.__spyname)

    def public_reveal(self): # Public function to access private functions
        return self.__reveal_spyname()

hanna2 = SpyName2("Hanne", 33, "Kisskorv")
# hanna2.get_spy_name() # Works
# # print(hanna2.__spyname) # cannot acccess
# print(hanna2.get_spy_name()) # runs hann2.get_spy_name, which returns the name, prints the return.



hanna2.__spyname = "Röfven" # Spyname can be directly changed?
print(hanna2.__spyname) # Now show the "modified spyname". This is now public, and is "Röfven"
print(hanna2.get_spy_name()) # Prints "Kisskorv" as it is the private spyname. Not modified by the change to "Röfven"
# print(hanna.__spyname) # This cannot be accessed though?

# When changing a private attribute, you need to use the correct set function (get to that later)
# If we modify using the normal hanna.__spyname = "New name", this creates a public attribute 
# that can be accessed using .__spyname.
# To get the ACTUAL spyname though, we must use get_spy_name(). This collects the private attribute

hanna2.set_spy_name("Kiss") # Actually changes the spyname, by running  the set-function inside the class
print(hanna2.get_spy_name())
print(hanna2.__spyname) # Still shows the public attribute "Röfven"

# We can also make functions private and access them with public functions
#print(hanna2.__reveal_spyname()) # Does not work. 
hanna2.public_reveal() # Runs public reveal, which in turn runs __reveal_spyname. __reveal_spyname prints the spyname, which is retuned in public_reveal.
# If we use print(hanna2.public_reveal()) we get "None" sinse the value retuned is allready a print.
# If __reveal_spyname() had a return statement instead, we would have to use print to print it.

