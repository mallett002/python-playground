
def main():
    # Sets
    my_set = {'Will', 38, 'Marcela', 33}
    print(my_set)

    # turn list into set with "set()"
    lst1 = ['abc', 123, 'def', 10.5, 62]
    set_from_list = set(lst1)
    print(set_from_list)

    # sets can't contain lists, other sets or dictionaries
    lst1.append(['quack'])
    # this_set_wont_work = set(lst1)

    # Accessing values:
    students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}

    if 'Chau' in students:
        print('Chau is in there!')
    
    # add an item:
    # can't update existing values, but can add/remove 
    students.add('George')
    print('George in there?', 'George' in students)

    # .update()
    # alters original set, does not return anything (returns None)
    teamPella = {'Will', 'Brad', 'Andrew', 'Nick', 'Matt', 'Jason'}
    teamPrincipal = {'Tom', 'Rebecca', 'Andy', 'Maarig'}

    teamPella.update(teamPrincipal)
    print('Pella is now: ', teamPella)

    # update takes any iterable (list, tuple, etc.)
    listPeople = ['Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry']

    teamPella.update(listPeople)
    print('Pella is now: ', teamPella)

    # .union()
    # takes iterable like update()
    # does not alter original sets, returns new set
    teamPella = {'Will', 'Brad', 'Andrew', 'Nick', 'Matt', 'Jason'}
    teamPrincipal = {'Tom', 'Rebecca', 'Andy', 'Maarig'}

    mergedTeam = teamPella.union(teamPrincipal)
    print('Unioned team is now', mergedTeam)

    # can use sets in for loops:
    for person in mergedTeam:
        print('Person: ', person)


if __name__ == '__main__':
    main()
