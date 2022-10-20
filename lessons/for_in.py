"""An example of for in syntax."""

names: list[str] = ["Tanveer", "Jason", "Puneet", "Rohan"]

#Example of iterating through names using while loop
print("While output: ")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

#The following for..in loop is the same as as the while loop above
print("For..in output: ")
for name in names:
    print(name)