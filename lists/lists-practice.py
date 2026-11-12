
backpack = []

while True: 
    print('What Items do you need for this Trip? ', str(len(backpack) + 1), '(Or enter nothing to stop)')
    item = input()
    if item == '':
        print('Looks like you have all you need')
        break # stops program after they enter nothing
    backpack = backpack + [item]
    print(backpack)

for item in backpack:
    print('', item)


# ---- Corrected version ----
backpack = []

while True:
    print('Item ' + str(len(backpack) + 1) + ' for your backpack (or enter nothing to stop):')
    item = input().strip()  # strip() removes spaces at the start and end
    if item == '':
        print('Looks like you have all you need')
        break
    if item in backpack:  # True if item is already in the list
        print('You already packed ' + item)
        continue  # skip the rest of the loop and ask again
    backpack.append(item)  # adds item to the end of the same list

print('Your backpack has:')
for item in backpack:
    print('  ' + item)
