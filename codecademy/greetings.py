def print_hello():
    print("hello world!")


def greet_someone():
    name = input("What's your name? ")
    hometown = input('Where are you from? ')
    
    # Can use String.format or f'' to format strings
    print('Nice to meet you {},'.format(name),f'from {hometown}')


def variables():
    # casting
    temp = str(97.5)
    print(type(temp))

    int_value = 4
    print(int_value)
    print(type(int_value))

    float_value = float(int_value)
    print(float_value)
    print(type(float_value))


def data_types():
    # bool
    # raining = True  
    # raining = bool('Fooey')
    # print(raining)

    # raining = bool(None) # 0, None or False
    # print(raining)

    temp = int(101.2)
    print(type(temp))

    temp = float(101.2)
    print(type(temp))

    temp = bool(101.2)
    print(type(temp))

    temp = str(101.2)
    print(type(temp))


def operators():
    # // Floor division
    # ex: x // y    "x divided by y, returning integer"

    # ** Exponentiation
    # ex: x ** y    "x raised to the power of y"
    x = 4

    # some examples
    x += 4  # x is 8
    x -= 4  # x is 0
    x *= 4  # x is 16
    x /= 4  # x is 1.0
    x %= 4  # x is 0

    print(x)

    # and, or, not
    x = 4
    y = 3

    if x > 2 and y > 1:
        print("yes")

    if x > 5 or y <= 3:
        print("howdy")
    
    if not(x > 2 and y > 1):
        print("quack") # no quack


def main():
    # greet_someone()
    # variables()
    # data_types()
    operators()


if __name__ == '__main__':
    main()