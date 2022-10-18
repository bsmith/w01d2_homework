united_kingdom = [
    {
        "name": "Scotland",
        "population": 5295000,
        "capital": "Edinburgh"
    },
    {
        "name": "Wales",
        "population": 3063000,
        "capital": "Swansea"
    },
    {
        "name": "England",
        "population": 53010000,
        "capital": "London"
    }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
def find_country_data(name):
    for country in united_kingdom:
        if country["name"] == name:
            return country
    raise ValueError(f"No such country as {name}")
wales_data = find_country_data("Wales")
wales_data["capital"] = "Cardiff"

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
ni_data = {
    "name": "Northern Ireland",
    "population": 1_811_000,
    "capital": "Belfast",
}
united_kingdom.append(ni_data)

# 3. Use a loop to print the names of all the countries in the UK.
for country in united_kingdom:
    print(f"Constituent country: {country['name']}")

# 4. Use a loop to find the total population of the UK.
total_population = 0
for country in united_kingdom:
    total_population += country["population"]

print(f"Total population of the UK is {total_population}")

# The python exception hierarchy and advice when to use each one
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy