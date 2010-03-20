import pystache
from models.post import Post

class Base(pystache.View):
  template_path = 'templates/posts'

  def __getattr__(self, name):
    if self.post:
      try:
        return self.post[name]
      except:
        AttributeError

class Index(Base):
  def posts(self):
    return Post.all()

class New(Base):
  pass

class Show(Base):
  def __init__(self, post):
    super(Show, self).__init__()
    self.post = post

  def title(self):
    return self.post['title']

  def untitled(self):
    return self.post['title'] == ''

  def anonymous(self):
    return self.post['author'] == ''
