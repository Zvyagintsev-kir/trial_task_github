import random
import string


class User(object):
    def __init__(self, user_name=None, user_email=None, user_password=None, validation_error=None):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.validation_error = validation_error

    @staticmethod
    def _create_data():
        random_sufix = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
        data = {
            "user_name": "testUserName-{}".format(random_sufix),
            "user_email": "testUserEmail-{}@test.com".format(random_sufix),
            "user_password": "Pass{}".format(random_sufix),
            "validation_error": ''
        }
        return data

    @classmethod
    def generate_random_user(cls):
        gen_data = cls._create_data()
        return cls(**gen_data)

    @classmethod
    def generate_user_with_empty_name(cls):
        gen_data = cls._create_data()
        gen_data["user_name"] = ''
        gen_data["validation_error"] = "Login can't be blank"
        return cls(**gen_data)

    @classmethod
    def generate_user_with_empty_email(cls):
        gen_data = cls._create_data()
        gen_data["user_email"] = ''
        gen_data["validation_error"] = "Email can't be blank"
        return cls(**gen_data)

    @classmethod
    def generate_user_with_empty_password(cls):
        gen_data = cls._create_data()
        gen_data["user_password"] = ''
        gen_data["validation_error"] = "Password can't be blank and is too short (minimum is 7 characters)"
        return cls(**gen_data)



 #   def generate_user_with_empty_name(self):
