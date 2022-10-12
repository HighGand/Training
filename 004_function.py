# Create new simple function
def simple_function():
    return 'Hello Word'
print(simple_function())

# Function with parameter
def parameter(name):
    return f'Hello {name}'
print(parameter('Tymek'))

# Simple calculator with use function
def calc():
    a = int(input('Please give to me number 1: '))
    b = int(input('Please give to me number 2: '))
    print('''What the math operation must doing?:
    1 - add '+'
    2 - subtraction '-'
    3 - multiplication '*'
    4 - division '/' ''')
    choice = int(input())
    if choice == 1:
        return a+b
    elif choice == 2:
        return a-b
    elif choice == 3:
        return a*b
    else:
        try:
            return a/b
        except ZeroDivisionError:
            print('Nie dzieli się przez zero cholero!!!')
print(calc())
