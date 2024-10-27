

def main():
    # dictionaries
    groceries = {
        'fruits': ['mangoes', 'bananas', 'kiwis'],
        'protein': ['beef', 'pork', 'salmon'],
        'carbs': ['rice', 'pasta', 'bread'],
        'veggies': ['lettuce', 'cabbage', 'onions']
    }

    # access with key
    print(groceries['carbs'])

    # updates
    groceries['deserts'] = ['cake', 'ice cream', 'cereal']
    print(groceries['deserts'])

    groceries['deserts'].append('crem brule')
    print(groceries['deserts'])

    # .len(): # of key-value pairs in dictionary
    print(len(groceries))

    # .update() updates dictionary with new dictionary
    # overwrites old with new with overlapping keys
    new_groceries = {
        'essentials': ['eggs', 'milk', 'bread'],
        'carbs': ['lasagna', 'whole grain pasta']
    }
    groceries.update(new_groceries)

    print(groceries)

    # .keys() & .values()
    groceries.keys()
    groceries.values()

    for key in groceries.keys():
        print('key: ', key)

    for val in groceries.values():
        print('val: ', val)



if __name__ == '__main__':
    main()