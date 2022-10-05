"""Demostrating of dictionries capabilities."""


#Declaring the type of dictionary
schools: dict[str, int]

#Intialize to an empty dictionary
schools = dict()

#Set a key-value pairing to a dictionary
schools["UNC"] = 19400
schools["Duke"] = 6917
schools["NCSU"] = 26150

#Print a dictionary literal representation
print(schools)

#Accessing a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

#Remove a key-value pair from dictionary by its key
schools.pop("Duke")

#Test for exsistence of key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

#Update/Resign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

#Demonstration of dictionary literals
#Empty dictionary literal 
schools = {} #Same as dict()
print(schools)

#Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

#What happens when a key does not exist
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
