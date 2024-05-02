
import random 

score = 0 
tries = 0 
answer = 0
human_input = 0 
option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]
def game():
    global option
    global human_input
    one = random.choice(option)
    print(f"first card   {one}")
    human_input = input("enter your first gess L or H? ")
    two = random.choice(option)
    if human_input.lower() == "l":
        if one > two:
            print(f"correct it was {two}")
            game()
        else:
            print(f"Wrong it was {two}")
    elif human_input.lower() == "h":
        if one < two:
            print(f"correct it was {two}")
            game()
        else:
            print(f"Wrong it was {two}")


game()
