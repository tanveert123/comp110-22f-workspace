"""EX03 - Wordle."""
__author__ = "730578741"

from xmlrpc.client import Boolean

def contains_char (word:str, char_search:str) -> bool:
    """when given two strings, the first of any length, the second a single character, it will return True if the single character of the second string is found at any index of the first string, and return False otherwise."""
    assert len(char_search) == 1

    #While loop thats returns True or False for whether character is found in the word.
    i: int = 0
    while i < len(word):
        if char_search == word[i]:
            return True 
        i += 1  
    return False

def emojified (guess:str, secret:str) -> str:
    """It will produce a string of emojis whose color codes the guess as opposed to the secret given two strings of equal length, the first being a guess and the second being a secret."""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    emoji: str = ""

    #
    while i < len(guess):

        if contains_char(guess[i], secret[i]) == True:
            emoji += GREEN_BOX
        else:
            character_exists: bool = False
            alt_idx: int = 0

            while character_exists is not True and alt_idx < len(secret):
                if contains_char(secret[alt_idx], guess[i]):
                    character_exists = True
                alt_idx += 1

            if character_exists is True:
                emoji += YELLOW_BOX

            if character_exists is False:      
                emoji += WHITE_BOX
        
        i += 1  

    print(emoji)

def input_guess (n:int) -> str:
    """It will request the user for an estimate and keep prompting them until they submit a guess of the expected length if given an integer "expected length" of a guess as a parameter."""
    
    attempt: str = input("Enter a " + str(n) + " character word: ")
    while len(attempt) != n:
        attempt = str(input("That was not 6 letters! Try again: "))
    return attempt

def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1

    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        input_main: str = input_guess(5)
        print(emojified(input_main, "codes"))
        if input_main == "codes":
            return print(f"You won in {i}/6 turns!")
        i += 1
    return print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()

       