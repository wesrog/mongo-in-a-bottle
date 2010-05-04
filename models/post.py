from lib.model import Model

class Post(Model):
  def untitled(self):
    return self.title == ''

  def anonymous(self):
    return self.author == ''

  def url(self):
    return '/posts/%s' % self._id
