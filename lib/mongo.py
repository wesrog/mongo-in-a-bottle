import pymongo
from pymongo import Connection, collection

class Model(object):
  def __init__(self, data=None):
    self.connection = Connection()
    self.db = self.connection.blog
    self.collection = self.db[self.__class__.__name__]
    self.data = data

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
    self.__class__.__base__().collection.save(data)

  def remove(self):
    id = collection.ObjectId(self.data['_id']) 
    self.__class__.__base__().collection.remove({'_id': id})

  @classmethod
  def last(cls):
    try:
      count = Model().collection.find().count()
      record = Model().collection.find()[count-1]
      return cls(record)
    except pymongo.errors.InvalidId:
      return None

  @classmethod
  def find_one(cls, id):
    try:
      id = collection.ObjectId(id)
      model = cls.__base__().collection.find_one({'_id': id})
      return cls(model)
    except pymongo.errors.InvalidId:
      return None

  @classmethod
  def all(cls):
    return [cls(item) for item in cls.__base__().collection.find()]
