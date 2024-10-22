
class UserInfo:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
    
    def check_username(self, username_to_check):
        if username_to_check == self.username:
            return True
 
        return False


def main():
    # Encapsulation: Wrapping variables and methods in one unit, e.g., a class
    user = UserInfo('user123', 'abc@def.ghi')

    # use object to access members
    print(user.username)

    # Use object of class's method to check username
    print(user.check_username('user123')) # --> True
    print(user.check_username('user456')) # --> False


if __name__ == '__main__':
    main()
