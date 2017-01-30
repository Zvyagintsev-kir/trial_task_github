import random
import string


class User(object):
    def __init__(self, user_name=None, user_email=None, user_password=None):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    @staticmethod
    def _create_data():
        random_sufix = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
        data = {
            "user_name": "testUserName-{}".format(random_sufix),
            "user_email": "testUserEmail-{}@test.com".format(random_sufix),
            "user_password": "Pass{}".format(random_sufix)
        }
        return data

    @classmethod
    def generate_random_user(cls):
        gen_data = cls._create_data()
        return cls(**gen_data)



 #   def generate_user_with_empty_name(self):
