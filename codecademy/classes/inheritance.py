class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def print_info(self):
      print(self.name)
      print(self.age)


# Inherits from the Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject = subject

        # Call the parent's constructor
        Person.__init__(self, name, age)


def main():
    marcela = Teacher('Marcela', 33, 'ESL')
    marcela.print_info()


if __name__ == '__main__':
    main()
