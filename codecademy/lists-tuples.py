
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

if __name__ == '__main__':
    main()
