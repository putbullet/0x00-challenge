class User():
    """User class"""

    def __init__(self):
        """Initialize a User instance."""
        self.__email = None

    @property
    def email(self):
        """Get the email address."""
        return self.__email

    @email.setter
    def email(self, value):
        """Set the email address."""
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self.__email = value

if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)

