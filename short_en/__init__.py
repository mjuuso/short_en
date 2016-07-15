import string
import random
import json


class Shortener(object):
    def __init__(self, base_url):
        self.urls = {}
        self.hash_length = 6
        self.base_url = base_url
        self.db_file = 'url.db'
        self.__load()
        pass

    def find(self, key):
        for h, u in self.urls.iteritems():
            if h == key:
                return u
        return None

    def create(self, url):
        hash = self.__generate_hash()
        self.urls[hash] = url
        self.__save()

        return self.base_url + hash

    def clear(self):
        self.urls = []
        self.__save()

    def __save(self):
        with open('url.db', 'w') as f:
            json.dump(self.urls, f)

    def __load(self):
        try:
            with open('url.db', 'r') as f:
                self.urls = json.load(f)
        except IOError:
            self.__save()

    def __generate_hash(self):
        hash = self.__hasher(self.hash_length)
        while self.find(hash):
            hash = self.__hasher(self.hash_length)
        return hash

    def __hasher(self, length):
        return ''.join(random.choice(string.ascii_lowercase +
                                     string.ascii_uppercase +
                                     string.digits)
                       for _ in range(length))
