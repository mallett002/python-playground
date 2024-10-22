def main():
    intro = 'My name is Will!'
    print(intro[0:2]) # --> My

    print(intro[-5:-1]) # -->  Will

    print(len(intro)) # --> 16

    print(intro.lower())
    print(intro.upper())
    print(intro.title()) # --> My Name Is Will!

    print(intro.split()) # splits into list of strings



if __name__ == '__main__':
    main()
