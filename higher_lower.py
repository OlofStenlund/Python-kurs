import random

score = 0
min_num = 0
max_num = 100
flag = 0


while flag == 0:
    random_num_1 = random.randint(min_num, max_num)
    print(f"The number is ", random_num_1)
    guess_input = input("Is the next number higher or lower?: ")
    random_num_2 = random.randint(min_num, max_num)
    number_var = random_num_2
    if guess_input == "<" and random_num_2 < random_num_1 or guess_input == ">" and random_num_2 > random_num_1:
        print("You were right!")
        print(f"The number was ", random_num_2)
        score = score+1
        print(f"Your score is ", score)
        number_var = random_num_2
        print(number_var)
    elif guess_input == "exit":
        flag = 1
    else:
        print("You were wrong!")
        print(f"The number was ", random_num_2)
        print(f"You got ", score, " point(s).")
        flag = 1
        


