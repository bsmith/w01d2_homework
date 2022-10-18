stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
linlithgow_idx = stops.index("Linlithgow")
stops.insert(linlithgow_idx, "Polmont")
#4. Print out the index position of "Linlithgow"
print("Linlithgow is at index", linlithgow_idx)
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
#6. Delete "Cumbernauld" from the list by index
cumbernauld_idx = stops.index("Cumbernauld")
stops.pop(cumbernauld_idx)
#7. Print the number of stops there are in the list
print(f"There are {len(stops)} stops")
#8. Sort the list alphabetically
stops.sort()
#9. Reverse the positions of the stops in the list
stops.reverse()
#10 Print out all the stops using a for loop
for stop in stops:
    print(f"Stopping at {stop}")

# Link to documentation for `list` class
# https://docs.python.org/3/library/stdtypes.html#list
# https://docs.python.org/3/library/stdtypes.html#typesseq-common
# https://docs.python.org/3/library/stdtypes.html#typesseq-mutable

# !!!! Don't confuse array and list!!!!
# WRONG Link to documentation for `array` class which lists all the methods like `index`
# WRONG https://docs.python.org/3/library/array.html
