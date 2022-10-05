"""EX06 - 'Choose Your Own Adventure'.""" 


__author__ = "730578741"


import random


point = 0
player: str
user_decision: str
THUMBS_UP: str = "\U0001F44D"
CHECK: str = "\U00002705"
THUMBS_DOWN: str = "\U0001F44E"
X_MARK: str = "\U0000274C"


def main() -> None:
    """Entry point to program."""
    greet()
    decision()
    game_loop()

def greet() -> None:
    """This is the greet function. Its main purpose is to greet the user as they begin to play the game."""
    print("Welcome to my game! This is a coinflip guessing game where you have to choose heads or tails. A score is tracked which represents how many times you got it correct!")
    global player
    player = input("What is your name? ")


def decision() -> None:
    """This is the decision function. Its main purpose is to find out what the user wants to do and execute that decision."""
    global user_decision
    global player
    user_decision = input(f"Hi there {player}! Would you like you to play the game, check your score, or end the game? (Please respond word-for-word with same capitalization - Play, Check Score, End): ")
    
    if "Play" in user_decision:
        play()
    elif "Check Score" in user_decision:
        check_score()
        decision()
    elif "End" in user_decision:
        check_score()
        print("Thanks for playing the game! Hopefully you enjoyed it!")
        exit()
    else:
        while user_decision != "Play" and user_decision != "Check Score" and user_decision != "End":
            user_decision = input(f"Try again {player}! Please respond word-for-word with same capitalization - Play, Check Score, End: ")


def play() -> None:
    """This is the play function. It runs when the user wants to play the game."""
    global player
    global point
    global THUMBS_UP
    global THUMBS_DOWN 
    global CHECK
    global X_MARK

    h_or_t: str = input(f"{player}, Please guess what side you think the coin will fall on (Heads/Tails): ")
    auto_generated = random.choice(["Heads", "Tails"])

    if auto_generated == h_or_t:
        print(f"Congrats! You guessed correctly! {THUMBS_UP}{CHECK}")
        increase_score(point)
    else:
        print(F"Wrong! You guessed incorrectly! {THUMBS_DOWN}{X_MARK}")


def increase_score(num: int) -> int:
    """This is the increase_score function. Its main purpose is to increase the 'point' variable for the score of the game."""
    global point
    point += 1


def game_loop() -> None:
    """This is the game_loop function. Its main purpose is to make the game continue to run until the user doesn't want to play."""
    while user_decision != "End":
        check_score()
        decision()


def check_score() -> None:
    """This is the check_score function. This runs when the user wannt to check his/her score."""
    global point
    print(f"Your score is: {point}")


if __name__ == "__main__":
  main()