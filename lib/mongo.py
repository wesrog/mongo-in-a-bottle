import pymongo
from pymongo import Connection, collection

class Model(object):
  def __init__(self):
    self.connection = Connection()
    self.db = self.connection.blog
    self.collection = self.db.posts

  def save(self):
    self.__class__.__base__().collection.insert(self.data)

  def remove(self):
    id = collection.ObjectId(self.data['_id']) 
    self.__class__.__base__().collection.remove({'_id': id})

  @classmethod
  def last(cls):
    try:
      model = cls.__base__().collection
      count = model.find().count()
      record = model.find()[count-1]
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
