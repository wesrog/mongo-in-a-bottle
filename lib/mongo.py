import pymongo
from pymongo import Connection, collection
import config.settings as s

class Model(object):
  def __init__(self, data=None):
    self.connection = Connection()
    self.db = self.connection[s.database]
    self.data = data

  def collection(self):
    return self.__class__.__name__.lower()

  def __getattr__(self, name):
    if name in self.data:
      try:
        return self.data[name]
      except:
        AttributeError

  def save(self, data=None):
    if not data:
      data = self.data
    else:
      data['_id'] = self.data['_id']
    #self.__class__.__base__().collection.save(data)
    self.db[self.collection()].save(data)

  def remove(self):
    id = collection.ObjectId(self.data['_id']) 
    self.db[self.collection()].remove({'_id': id})

  @classmethod
  def last(cls):
    try:
      count = Model().db[cls().collection()].find().count()
      record = Model().db[cls().collection()].find()[count-1]
      return cls(record)
    except pymongo.errors.InvalidId:
      return None

  @classmethod
  def find_one(cls, id):
    try:
      id = collection.ObjectId(id)
      model = Model().db[cls().collection()].find_one({'_id': id})
      return cls(model)
    except pymongo.errors.InvalidId:
      return None

  @classmethod
  def all(cls):
    return [cls(item) for item in Model().db[cls().collection()].find()]
