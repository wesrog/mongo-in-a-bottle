import lib.mongo
from lib.mongo import Model

class Post(Model):
  def untitled(self):
    return self.title == ''

  def anonymous(self):
    return self.author == ''

  def url(self):
    return '/posts/%s' % self._id
