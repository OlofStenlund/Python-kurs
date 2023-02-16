import random
from function_db import call_db

# Query to create high score table
create_highscore_table = """
CREATE TABLE IF NOT EXISTS high_scores(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL      
)
"""
# Wuery to see high scores
get_highscore_query = """
SELECT name, score FROM high_scores ORDER BY score DESC LIMIT 5
"""
save_score = """
    INSERT INTO high_scores(
    name,
    score
    )
    VALUES(
    ?,
    ?
    )
"""
call_db(create_highscore_table)

score = 0
min_num = 0
max_num = 100
flag = 0

def print_highscores():
    highscores = call_db(get_highscore_query)
    # Loop to print highscores
    for i in highscores:
        name, score = i
        print(f"{name} {score}")

print_highscores()

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
        name = input("Enter your name: ")       
        call_db(save_score, name, score)
        flag = 1
        


