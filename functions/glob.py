def spam():
    # global eggs
    print(eggs) # ERROR!
    eggs = 'spam local'


eggs = 'global'
spam()

# error because pring comes before eggs is defined

