#from lib.model import Model
from mongoengine import *
import config.settings as s
connect(s.database)

class Post(Document):
    title = StringField(required=True)
    author = StringField()
    body = StringField()

    def build(self, params):
        for k in params.keys():
            if params[k] != '':
                self.__setitem__(k, params[k])
