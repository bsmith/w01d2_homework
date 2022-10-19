users = {
    "Jonathan": {
        "twitter": "jonnyt",
        "lottery_numbers": [6, 12, 49, 33, 45, 20],
        "home_town": "Stirling",
        "pets": [
            {
                "name": "fluffy",
                "species": "cat"
            },
            {
                "name": "fido",
                "species": "dog"
            },
            {
                "name": "spike",
                "species": "dog"
            }
        ]
    },
    "Erik": {
        "twitter": "eriksf",
        "lottery_numbers": [18, 34, 8, 11, 24],
        "home_town": "Linlithgow",
        "pets": [
            {
                "name": "nemo",
                "species": "fish"
            },
            {
                "name": "kevin",
                "species": "fish"
            },
            {
                "name": "spike",
                "species": "dog"
            },
            {
                "name": "rupert",
                "species": "parrot"
            }
        ]
    },
    "Avril": {
        "twitter": "bridgpally",
        "lottery_numbers": [12, 14, 33, 38, 9, 25],
        "home_town": "Dunbar",
        "pets": [
            {
                "name": "monty",
                "species": "snake"
            }
        ]
    }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print("Jonathan's Twitter handle:", users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print("Erik's hometown:", users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print("Erik's lottery numbers:", users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
monty_species = 'not sure'
avril_pets = users["Avril"]["pets"]
for pet in avril_pets:
    if pet["name"] == "monty":
        monty_species = pet["species"]
        break
print("Avril's pet Monty is a", monty_species)

# 5. Get the smallest of Erik's lottery numbers
print("Erik's smallest lottery number is",
    sorted(users["Erik"]["lottery_numbers"])[0])
# Could also write a for-loop, but don't forget `min`!

# 6. Return an list of Avril's lottery numbers that are even
print("Avril's even lottery numbers:",
    [num for num in users["Avril"]["lottery_numbers"] if num % 2 == 0])

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append(
    {
        "name": "fluffy",
        "species": "dog"
    }
)

#users["Erik"]["pets"] += [{"name" : "fluffy", "species": "dog"}]
#print(users["Erik"]["pets"])

print("Erik's new lottery numbers:", users["Erik"]["lottery_numbers"])
print("Erik's new hometown:", users["Erik"]["home_town"])
print("Erik's new pets:", users["Erik"]["pets"])

# 10. Add another person to the users dictionary
new_name = "Ben"
new_user = {
    "twitter": "bsmith",
    "lottery_numbers": [1, 3, 7, 24, 31],
    "home_town": "Edinburgh",
    "pets": [
        {
            "name": "quacky",
            "species": "rubberduck"
        }
    ]
}
users[new_name] = new_user

# users.update({
#     "twitter": "etc...",
# })

print("We have a new person:", users["Ben"])

# `array.sort`` sort's stuff in place
# the `sorted` function takes an iterable and returns a new sorted list
# see https://docs.python.org/3/library/functions.html#sorted

# list comprehensions tutorial
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions