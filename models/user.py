import random
import string


class User(object):
    def __init__(self, user_name=None, user_email=None, user_password=None):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.random_sufix = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))

    def generate_random_user(self):
        self.user_name = "testUserName-{}".format(self.random_sufix)
        self.user_email = "testUserEmail-{}@test.com".format(self.random_sufix)
        self.user_password = "Pass{}".format(self.random_sufix)

 #   def generate_user_with_empty_name(self):
