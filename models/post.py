import pymongo
from pymongo import Connection, collection

connection = Connection()
db = connection['blog']
posts = db.posts

class Post:
  @staticmethod
  def all():
    return posts.find()

  @staticmethod
  def find_one(id):
    try:
      id = collection.ObjectId(id)
      return posts.find_one({'_id': id})
    except pymongo.errors.InvalidId:
      return None

  @staticmethod
  def remove(id):
    posts.remove({'_id': collection.ObjectId(id)})

  @staticmethod
  def insert(post):
    if not post['author'] == '':
      posts.insert(post)
