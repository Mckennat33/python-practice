
catNames = []

while True: # keeps going until the user enters nothing
    print('Enter the name of a Cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

print('The cat names are')


for name in catNames:
    print(' ' + name)  
