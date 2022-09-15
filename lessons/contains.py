"""Example implementing a list utility function."""

# Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
# Gameplan:
# 1. start with the first index
    i: int = 0
# 2. Loop through every index
    while i < len(haystack):
#   2a. Test if item at index equal to needle
        if needle == haystack[i]:
#       2a. True Return True! We found it!
            return True
        i += 1
#3. Return False
    return False
