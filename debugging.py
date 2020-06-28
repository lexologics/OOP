
def add(x, y):
    sum = x + y
    return sum

if __name__ == '__main__':
    #x = input('Num 1 : ')
    # corrrected code:
    x = int(input('Num 1 : '))
    
    #y = input('Num 2 : ')
    # corrrected code:
    y = int(input('Num 2 : '))
    z = add(x, y)
    print(z)
    
