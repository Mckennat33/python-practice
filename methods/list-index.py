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

# sort
# - on strings it will sort alpha by first letter / not actually alpha 
numbers = [4, 1, 0, -5, 10, 9, 23]
numbers.sort()
print(numbers)
# you cant put a variable to sort n = numbers.sort()
# cant sort lists that have number values and strings
# - Sort true and false


import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
