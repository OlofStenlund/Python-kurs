import requests
from api import Todo


def url(route: str):
    return f"http://127.0.0.1:8000{route}"



def print_menu():
    print("""
    1: Add todo
    2: Get todo
    3: Delete todo
    4: Update todo
    5: Exit
    """)


def add_todo():
    print("Adds todo")
    title = input("Todo title: ")
    description = input("Todo description: ")
    new_todo = Todo(title=title, description=description)
    res = requests.post(url("/add_todo"), json=new_todo.dict()) # add_todo goes into "route" in baseurl
    print(res.json())

def get_todo():
    todos = []
    print("get todo")
    res = requests.get(url("/get_todos"))
    if not res.status_code == 200: # check that code is 200, ie it was successful. If not, return
        return
    data = res.json()
    for todo in data: # Todo is a dixt {"title": "aaaa", "description": "bbbb"}
        #**todo unpacks the variable into keywordarguments, since what is returned is a dict.
        todo = Todo(**todo) # breaks down the dict and unpack into the right name below?
        # todo = Todo(title = todo["title"], description = todo["description"]) # the same thing
        print("_________")
        print(todo.title) # Print the word with key title
        print(todo.description) # Print the word with the key description
        todos.append(todo)
    return todos

def delete_todo():
    print("delete todo")
    todo_to_delete = input("id of todo you wish to delete: ")
    if not str.isdigit(todo_to_delete):
        print("Please enter a valid choice.")
        return 
    res = requests.delete(url(f"/delete_todo/{todo_to_delete}"))
    print(res.json())

def update_todo(todos):
    print("update todo")
    todo_to_update = input("id of todo you wish to update: ")
    if not str.isdigit(todo_to_update):
        print("Please enter a valid choice.")
        return
    todos.index()
    res = requests.put(url(f"/update_todo/{id}", json=""))
    print(res.json())


def main():
    todos = []
    print_menu()
    choice = input("Please chose an action: ") # Take input
    choice = choice.strip() # Trim the input
    if not str.isdigit(choice): # If input is not a number...
        print("Please enter a valid option") # ...print this
        return 
    
    # Since we now are sure the input is a number, we don't need to check it again
    # Similar to a if/elif or switch/case
    match int(choice):
        case 1:
            add_todo()
        case 2:
            todos = get_todo()
        case 3: 
            delete_todo()
        case 4:
            update_todo()
        case 5:
            exit()
        case _:
            print("Please enter a valid option")
    pass
    


# While the name of the file is __main__ it runs
# It is only main in this file, and not when imported into other files
# Avoids while loops in main() somehow?
while __name__ == "__main__":
    main()