#from lib.model import Model
from mongoengine import *
import config.settings as s
connect(s.database)

class Post(Document):
  title = StringField(required=True)
  author = StringField()
  body = StringField()
