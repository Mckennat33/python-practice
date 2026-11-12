

def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1)) # not called error hits then runs to except clause
    
except ZeroDivisionError:
    print('error invalid argument')





