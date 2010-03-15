import pystache
from models.post import Post

class Base(pystache.View):
  template_path = 'views/posts'

class Index(Base):
  def posts(self):
    return Post.all()

class Show(Base):
  post = None

  def title(self):
    if self.post:
      return self.post['title']

  def author(self):
    if self.post:
      return self.post['author']

  def body(self):
    if self.post:
      return self.post['body']
