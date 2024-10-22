class ClassSchedule:
    def __init__(self, course, instructor, building, number):
        self.course = course # public
        self.instructor = instructor # public
        self._building = building # protected (note the prefixed "_")
        self.__number = number # protected (note the prefixed "__")

    def display_course(self):
        print(f'Course: {self.course}, Instructor: {self.instructor}')


def main():
   # all members public by default 
   sched = ClassSchedule('Chemistry', 'Mr. Doe', 'Neeman Hall', 'CHEM101')

   sched.display_course()
   print(sched.course) # has access (public by default)
   print(sched._building) # can access protected member, but you shouldn't
   print(sched.__number) # get error trying to access private member


if __name__ == '__main__':
    main()
