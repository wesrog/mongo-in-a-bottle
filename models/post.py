import pymongo
from pymongo import Connection, collection
import lib.mongo
from lib.mongo import Model

class Post(Model):
  def __init__(self, data):
    self.data = data

  def __getattr__(self, name):
    if name in self.data:
      try:
        return self.data[name]
      except:
        AttributeError

  def untitled(self):
    return self.title == ''

  def anonymous(self):
    return self.author == ''

  def url(self):
    return '/posts/%s' % self._id
