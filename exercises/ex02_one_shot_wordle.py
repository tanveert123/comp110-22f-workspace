"""EX02 - One-Shot Wordle."""

__author__ = "730578741"

# Asking user for their 6-letter word guess
word: str = str(input("What is your 6-letter guess: "))

# Established secret word
secret_word: str = "python"

# While loop which prints message if length of user input word is not equal to the length of secret word
while len(word) != len(secret_word):
    word = str(input("That was not 6 letters! Try again: "))

# Loop that works only if length of user input word is equal to the length of secret word
if len(word) == len(secret_word):
    # Creating emoji for future use. It makes a white box, yellow box, and green box.
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    index_word: str = word[i]
    emoji: str = ""

# While loop that iterates through every letter of user input word to figure out if it prints green, yellow, or white box
    while i < len(word):

        # Loop that works only if the value of the index of the secret word is equal to the value of the index of the user input word. It prints green box to the empty 'emoji' string.
        if secret_word[i] == word[i]:
            emoji += GREEN_BOX
        else:
            character_exists: bool = False
            alt_idx: int = 0

            # Loop that works to see if the index of the user input word is found in a different index of the secret word. Stores information through boolean variable called 'character_exists'. 
            while character_exists is not True and alt_idx < len(secret_word):
                if secret_word[alt_idx] == word[i]:
                    character_exists = True
                alt_idx += 1

            # Loop that works if 'character_exists' value is True. It prints yellow box to the empty 'emoji' string.
            if character_exists is True:
                emoji += YELLOW_BOX
        
            # Loop that works if 'character_exists' value is False. It prints white box to the empty 'emoji' string.
            if character_exists is False:      
                emoji += WHITE_BOX
        i += 1  

# Prints the emoji string which includes the green, yellow, and white boxes.        
print(emoji)

# c      Loop that prints a message if the user input word matches the secret word. It also prints a message if they do not match.  
if word == "python":
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")