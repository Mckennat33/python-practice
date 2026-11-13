# Method is the same thing as a function, except it is called on a value. If you had a list called backpack, you would call index on it. 

# prints the index of hand soap
backpack = ['Toothbrush', 'toothpaste', 'hand soap']
example = backpack.index('hand soap')
print(example)

# adding values to list with append() & insert()
# append()
costco = ["Annalise", "Lindsay", "Thomas"]
costco.append("Logan")
print(costco)

# insert()
costco.insert(0, "Phil")
print(costco)

# remove
# - if name not in list you will get error
costco.remove("Phil")
print(costco)
