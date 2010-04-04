import pymongo
from pymongo import Connection, collection
import lib.mongo
from lib.mongo import Model
#import parsedatetime.parsedatetime as pdt
#import parsedatetime.parsedatetime_consts as pdc

#connection = Connection()
#db = connection['blog']
#posts = db.posts

class Post(Model):
  def __init__(self, data):
    self.data = data

  @staticmethod
  def all():
    psts = []
    for p in Model().collection.find():
      psts.append(
          dict(
            _id       = p['_id'],
            author    = p['author'],
            title     = p['title'],
            untitled  = p['title'] == '',
            anonymous = p['author'] == '',
            url       = '/posts/%s' % p['_id']
          )
      )
    return psts
    #return posts.find()

