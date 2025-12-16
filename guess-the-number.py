from random import randint
from art import logo
print(logo)

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0

def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You go it! The answer was {actual_answer}")

def set_difficulty():
    level=input("Choose a difficulty level: Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to Guessing Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left.")
        guess = int(input("Make a guess: "))
        turns=check_answer(guess, answer,turns)
        if turns == 0:
            print(f"You lose! The correct answer was {answer}")
            return
        elif guess!=answer:
            print("guess again")


game()
