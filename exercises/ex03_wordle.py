"""EX03 - Wordle.""" 


__author__ = "730578741"

check_val: bool = False


def contains_char(char_Length: str, char_Letter: str) -> bool:
    """When given two strings, the first of any length, the second a single character, it will return True if the single character of the second string is found at any index of the first string, and return False otherwise."""
    assert len(char_Letter) == 1
    i: int = 0

    while check_val is not True and i < len(char_Length):
        if char_Length[i] is char_Letter:
            check_val is True
            return True 
        i += 1  
    return False


def emojified(guess: str, secret: str) -> str:
    """It will produce a string of emojis whose color codes the guess as opposed to the secret given two strings of equal length, the first being a guess and the second being a secret."""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    emoji: str = ""

    while i < len(secret):

        if guess[i] == secret[i]:
            emoji += GREEN_BOX
            i += 1
        else: 
            if contains_char(secret, guess[i]):
                emoji += YELLOW_BOX
                i += 1
            else:
                emoji += WHITE_BOX
                i += 1
    return emoji


def input_guess(n: int) -> str:
    """It will request the user for an estimate and keep prompting them until they submit a guess of the expected length if given an integer "expected length" of a guess as a parameter."""
    attempt: str = input("Enter a " + str(n) + " character word: ")
    while len(attempt) != n:
        attempt = input(f"That was not {n} letters! Try again: ")
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

       