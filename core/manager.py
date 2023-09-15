# # todo : use base64 for create short url
import string
from flask import request
from random import choice
from core import app, db
from core.models import ShortUrls


class Manager:
    def generate_short_id(self, ):
        """Function to generate short_id of 8 of characters"""
        return ''.join(choice(string.ascii_letters+string.digits) for _ in range(8))
    
    def add_newurl(self, new_url: ShortUrls):
        db.session.add(new_url)
        db.session.commit()
        hits = new_url.hits
        short_url = request.host_url + new_url.short_id
        return [short_url, hits]