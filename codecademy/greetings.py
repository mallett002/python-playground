def print_hello():
    print("hello world!")

def strings():
    name = 'Billium'
    town = 'Whoville'

    str1 = '{} is from {}'.format(name, town)
    str2 = f'{name} is from {town}'

    print(str1)
    print(str2)



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


def if_statements():
    score = 82

    if score >= 92:
        print('Your final grade is an A')
 
    elif score >= 85:
        print('Your final grade is a B')
    
    elif score >= 70:
        print('Your final grade is a C')
    
    else:
        print('Talk with your instructor about your grade!')


def for_loops():
    nums = [1, 2, 3, 4, 5]

    for num in nums:
        print(num + 1)

    # do something 3 times:
    for i in range(3):
        print(i)


def while_loops():
    i = 1

    while i < 6:
        print(i)
        i += 1

def controlling_loops():
    names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

    print("pass keyword:")
    # Pass: place in condition, if true, nothing gets executed
    # similar to continue, but does not skip to next iteration
    for name in names:
        if 'j' in name.lower():
            pass
        else:
            print(name)

    print("\nbreak keyword:")

    for name in names:
        if 'h' in name.lower():
            break
        else:
            print(name)
    
    print("\ncontinue keyword:")
    # continue skips to next iteration

    for name in names:
        if 'm' in name.lower():
            continue
        else:
            print(name)


def error_handling():
    nums = [5, 2, 3, 10]

    try:
        avg = sum(nums) / len(nums)

        print('Avg:', avg)

    except:
        print('something went wrong')

    finally:
        print('you did it')


def factorial(num):
    print("num: ", num)

    if num == 1:
        return 1

    return num * factorial(num - 1)


def lambdas():
    #lambda [args]: [expression]

    square_lambda = lambda x: x ** 2

    greeting = lambda name: f"Hello, {name}!"

    # use with lists
    numbers = [1, 2, 3, 4, 5]

    # map
    mapped = list(map(lambda x: x ** 2, numbers))
    print(f"mapped {mapped}")

    # filter
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filtered {filtered}")

    # sorted (list of tuples)
    students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)]
    
    sortedStudents = sorted(students, key=lambda x: x[2])
    print(f"sortedStudents {sortedStudents}")


class Dog:
    # this is an empty class
    pass


def main():
    # strings()
    # greet_someone()
    # variables()
    # data_types()
    # operators()
    # if_statements()
    # for_loops()
    # while_loops()
    # controlling_loops()
    # error_handling()
    # print(factorial(5))
    lambdas()


if __name__ == '__main__':
    main()

