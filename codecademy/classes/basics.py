
class Dog:
    # this is an empty class
    pass

class ClassSchedule:
    # constructor (needs to be named this __init__)
    def __init__(self, course):
        self.course = course

    def __del__(self):
        print('you successfully deleted your schedule')


def main():
    # pepper = Dog()
    # print(pepper)

    sched = ClassSchedule('Chemistry')
    print(sched.course)

    del sched


if __name__ == '__main__':
    main()
