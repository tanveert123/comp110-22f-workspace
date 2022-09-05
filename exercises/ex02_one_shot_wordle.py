"""EX02 - One-Shot Wordle."""

__author__ = "730578741"

#
word: str = str(input("What is your 6-letter guess: "))
secret_word: str = "python"

while len(word) != len(secret_word):
    word: str = str(input("That was not 6 letters! Try again: "))

if len(word) == len(secret_word):
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    index_word: str = word[i]
    emoji: str = ""

    while i < len(word):
        if secret_word[i] == word[i]:
         emoji += GREEN_BOX
        else:
            character_exists: bool = False
            alt_idx: int = 0

            while character_exists != True and alt_idx < len(secret_word):
                if secret_word[alt_idx] == word[i]:
                    character_exists = True
                alt_idx += 1
        
            if character_exists == True:
                emoji += YELLOW_BOX
        
            if character_exists == False:      
                emoji += WHITE_BOX
        i+=1  
           
print(emoji)
      
if word == "python":
        print("Woo! You got it!")
else:
        print("Not quite. Play again soon!")