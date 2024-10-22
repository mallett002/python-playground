def tuples():
    my_tupe = ('hi', 123, 'fooey', 45.9)
    one_item_tuple = (1,) # needs a comma at the end
    nums = (3, 9, 10, 1, 30, 4)
    colors = ('orange', 'blue', 'red', 'green')

    # accessig items
    print(my_tupe[3]) # --> 45.9
    print(my_tupe[1:3]) # --> ('fooey', 45.9)

    # len(): gets the length
    print(len(my_tupe))

    # max(): gets tuple's maximum value
    print(max(nums))
    print(max(colors)) # sorted alphabetically ascending

    # min(): gets tuple's min value
    print(min(nums))
    print(min(colors)) # sorted alphabetically ascending

    # index(): finds the index of the provided arg
    print(colors.index('red')) # --> 2

    # count(): Gets number of occurances of the tuple
    more_colors = ('red', 'blue', 'red')
    print(more_colors.count('red')) # --> 2


def lists():
    lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
    lst2 = [0, 1, 2, 3, 4]
    lst3 = ['I like sushi so much!', 'I do not like curry']

    # Slice the list (returns new list):
    print(lst1[0:1]) # --> [62, ['g', 'h', 'i']]

    # get item at index 0:
    print(lst1[0])

    # .append()
    lst3.append('ribs are good too')
    print(lst3)

    # .remove()
    lst3.remove('ribs are good too')
    print(lst3)

    # .pop(index: int)
    # removes item at index. if no index, removes last item
    print(lst2)
    print(lst2.pop(2)) # --> returns 2
    print(lst2)
    print(lst2.pop()) # --> returns 4
    print(lst2)


def main():
    # lists()
    tuples()

if __name__ == '__main__':
    main()
