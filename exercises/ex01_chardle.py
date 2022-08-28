"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730578741"

word: str = str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = str(input("Enter a single character: "))
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)

count: int = 0
if letter == word[0]:
    print(letter + " found at index 0")
    count+=1
if letter == word[1]:
    print(letter + " found at index 1")
    count+=1
if letter == word[2]:
    print(letter + " found at index 2")
    count+=1
if letter == word[3]:
    print(letter + " found at index 3")
    count+=1
if letter == word[4]:
    print(letter + " found at index 4")
    count+=1

if count == 1:
    print(str(count) + " instance of " + letter + " found in " + word)
elif count > 1:
    print(str(count) + " instances of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)