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
    return not self.empty()

  def empty(self):
    return len(self.post()) == 0

  def post(self):
    posts = Post.all()
    for p in posts:
      p.data['untitled'] = p.untitled()
      p.data['anonymous'] = p.anonymous()
      p.data['url'] = p.url()
    return [p.data for p in posts]

class New(Base):
  def post(self):
    return Post()

class Edit(Base):
  def __init__(self, post):
    super(Edit, self).__init__()
    self.post = Post(post.data)

class Show(Base):
  def __init__(self, post):
    super(Show, self).__init__()
    self.post = Post(post.data)
