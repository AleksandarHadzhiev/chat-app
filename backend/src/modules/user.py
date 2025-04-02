class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


    def set_username(self, username):
        self.username = username

    def fetch_from_db(self, email, password, username, id):
        self.id = id
        self.__init__(email=email, password=password)
        self.set_username(username=username)
                      