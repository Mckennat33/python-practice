# # looping through a range 
# for i in range(4):
#     print(i) # prints 0, 1, 2, 3. 0 is considered the start

# # This will have the same output 
# for i in [0, 1, 2, 3]: 
#     print(i)

# # Technique in a for loop to interate over the indexes of a list
# supplies = ['pens', 'staplers', 'flame throwers', 'binders']
# for i in range(len(supplies)): 
#     # len will iterate over the index and supplies[i] is asking what is sitting at each index. 
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# # In and not in Operator 
# spam = ['hello', 'hi', 'howdy', 'heyas']
# 'cat' in spam # 16 & 17 will only work in the terminal A: false

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print("Enter a pet name")
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')