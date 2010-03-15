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
    return posts.find_one({'_id': collection.ObjectId(id)})

  @staticmethod
  def remove(id):
    posts.remove({'_id': collection.ObjectId(id)})

  @staticmethod
  def insert(post):
    if not post['author'] == '':
      posts.insert(post)
