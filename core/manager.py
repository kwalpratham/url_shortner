# # todo : use base64 for create short url


import string
from random import choice


class Manager:
    def generate_short_id():
        """Function to generate short_id of specified number of characters"""
        return ''.join(choice(string.ascii_letters+string.digits) for _ in range(8))