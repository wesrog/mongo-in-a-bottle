import pystache
from models.post import Post

class Base(pystache.View):
  template_path = 'templates/posts'

  def __getattr__(self, name):
    if self.post:
      try:
        if name in self.post.data:
          return self.post.data[name]
        else:
          return self.post.__getattribute__(name)()
      except:
        AttributeError

class Index(Base):
  def posts(self):
    # return True if not empty
    return True

  def post(self):
    posts = Post.all()
    for p in posts:
      p.data['untitled'] = p.untitled()
      p.data['anonymous'] = p.anonymous()
      p.data['url'] = p.url()
    return [p.data for p in posts]

class New(Base):
  pass

class Show(Base):
  def __init__(self, data):
    super(Show, self).__init__()
    self.post = Post(data)
