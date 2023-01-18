# Can I get the class and functions into a separate file please?
# Would be nice to be able to import them
# from class_calculator import Calculator
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        return a / b


def choose_calculation():
    calc = input("What calculation? +, -, *, /")
    return calc
    
def collect_numbers():
    inp1 = input("give me a number")
    inp2 = input("Give me another")
    return[inp1, inp2]

def collect_number_reuse(a):
    checking = True
    while checking == True:
        inp2 = input("Give me another")
        if inp2.isnumeric():
            return[a, int(inp2)]
        else: 
            continue

def verify_numbers(a):
    checking = True
    while checking == True:

        if a[0].isnumeric() and a[1].isnumeric(): 
            return [int(a[0]), int(a[1])]
            break
        else:
            print("Nej du")
            continue

def play_func(meth, inp):
    if meth == "+":
        res1 = Calculator.add(inp[0], inp[1])
    elif meth == "-":
        res1 = Calculator.subtract(inp[0], inp[1])
    elif meth == "*":
        res1 = Calculator.multiply(inp[0], inp[1])
    elif meth == "/":
        res1 = Calculator.divide(inp[0], inp[1])
    return res1

run = True
quitgame = False
while True:
    if quitgame == True:
        break
    if run == True:
        userinput: list = verify_numbers(collect_numbers())
        resultat = play_func(choose_calculation(), userinput)
        keepgoing = input(f"The result is {resultat}. Do you want to continue? (y/n)")
    elif run == False:
        userinput = list(collect_number_reuse(resultat))
        choose_calculation()
        resultat = play_func(choose_calculation(), userinput)
        keepgoing = input(f"The result is {resultat}. Do you want to continue? (y/n)")
    if keepgoing == "n":
        quitgame = True
        break
    elif keepgoing  == "y":
        pass
    else:
        continue
    use_result = input(f"Would you like to use {resultat} in the next calculation? y/n")
    if use_result == "n":
        pass
        run = True
    elif use_result == "y":
        run = False








# run = True
# while True:
#     if run == True:
#         userinput: list = verify_numbers(collect_numbers())
#         resultat = play_func(Calculator.choose_calculation())
#         carryon = input(f"The result is {resultat}. Do you want to continue? (y/n)")
#         if carryon == "n":
#             break
#         elif carryon == "y":
#             pass
#         else:
#             continue
#         use_result = input("Would you like to use {resultat} in the next calculation? y/n")
#         if use_result == "n":
#             pass
#             run = True
#         elif use_result == "y":
#             run = False
#     elif run == False:
#         print(resultat)
#         userinput = list(collect_number_reuse(resultat))
#         resultat = play_func(Calculator.choose_calculation())
#         carryon = input(f"The result is {resultat}. Do you want to continue? (y/n)")
#         if carryon == "n":
#             break
#         elif carryon == "y":
#             pass
#         else:
#             continue
#         use_result = input("Would you like to use {resultat} in the next calculation? y/n")
#         if use_result == "n":
#             pass
#             run = True
#         elif use_result == "y":
#             run = False
