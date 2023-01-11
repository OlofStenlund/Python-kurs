    # Create a calculator
print("This is the calculator af doom")

def main():
    
    def addition_calc(a, b):
        return(a+b)
    
    def subtraction_calc(a, b):
        return(a-b)

    def multiplication_calc(a, b):
        return(a*b)

    def division_calc(a, b):
        return(a/b)
    
    def collect_numbers():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return[num1, num2]

    def collect_numbers_reuse():
        num1 = calc_res
        num2 = int(input("Enter the second number: "))
        return[num1, num2]

    def choose_calc():
        return(input("What calculation would you like to make: +, -, *, or /"))

    def continue_playing():
        cont = input("Would you like to continue? (y/n)")
        if cont == "y":
            return("y")
        elif cont == "n":
            return("n")

    def run_no_reuse():
        calc_chosen = choose_calc()
        if calc_chosen == "+":
            inputs_from_user = collect_numbers()
            calc_res = addition_calc(inputs_from_user[0], inputs_from_user[1])
        elif calc_chosen == "-":
            inputs_from_user = collect_numbers()
            calc_res = subtraction_calc(inputs_from_user[0], inputs_from_user[1])
        elif calc_chosen == "*":
            inputs_from_user = collect_numbers()
            calc_res = multiplication_calc(inputs_from_user[0], inputs_from_user[1])
        elif calc_chosen == "/":
            inputs_from_user = collect_numbers()
            calc_res = division_calc(inputs_from_user[0], inputs_from_user[1])
        return int(calc_res)

    def run_with_reuse():
        calc_chosen = choose_calc()
        if calc_chosen == "+":
            inputs_from_user = collect_numbers_reuse()
            calc_res = addition_calc(inputs_from_user[0], inputs_from_user[1])
        elif calc_chosen == "-":
            inputs_from_user = collect_numbers_reuse()
            calc_res = subtraction_calc(inputs_from_user[0], inputs_from_user[1])
        elif calc_chosen == "*":
            inputs_from_user = collect_numbers_reuse()
            calc_res = multiplication_calc(inputs_from_user[0], inputs_from_user[1])
        elif calc_chosen == "/":
            inputs_from_user = collect_numbers_reuse()
            calc_res = division_calc(inputs_from_user[0], inputs_from_user[1])
        return int(calc_res)

    run = True
    while True:
        if run == True:
            calc_res = run_no_reuse()
            print("The result is: ", calc_res)
            cont = continue_playing()
            if cont == "n":
                break
            elif cont == "y":               
                reuse = input("Would you like to use the result as your first number in the next calculation? (y/n)")
                if reuse == "n":
                    pass
                elif reuse == "y":
                    run = False
        elif run == False: 
            calc_res = run_with_reuse()
            print("The result is: ", calc_res)
            cont = continue_playing()
            if cont == "n":
                break
            reuse = input("Would you like to use the result as your first number in the next calculation? (y/n)")
            if reuse == "n":
                run = True
            elif reuse == "y":
                pass

main()


    # # This block contains attempts to validate the input. 
    # # Make sure to look int "isinstance"
    # def collect_numbers():
    #     num1 = int(input("Enter the first number: "))
    #     #print(isinstance(int(num1), int))
    #     #if isinstance(num1, int):
    #     #    pass
    #     #else:
    #     #    print("Invalid, must be a number.") 
    #     num2 = int(input("Enter the second number: "))
    #     #if type(num2) == int:
    #     #    pass
    #     #else:
    #     #    print("Invalid, must be a number.") 
    #     return[num1, num2]






