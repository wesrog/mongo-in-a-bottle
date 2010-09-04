import pystache
from models.post import Post

class BaseView(pystache.View):
  template_path = 'templates/posts'

  def url(self):
    return '/posts/%s' % self.id

  def id(self):
    return self.post.id

  def author(self):
    return self.post.author

  def title(self):
    return self.post.title

  def body(self):
    return self.post.body

  def untitled(self):
    return self.post.title == '' or self.post.title is None

  def anonymous(self):
    return self.post.author == '' or self.post.author is None

class Index(BaseView):
  def post(self):
    posts = []
    for post in Post.objects:
      data = post._data
      data.update({'untitled': post.title == '' or post.title is None})
      data.update({'anonymous': post.author == '' or post.author is None})
      data.update({'url': '/posts/%s' % post.id})
      posts.append(data)
    return posts

  def posts(self):
    return self.post_count > 0

  def post_count(self):
    return Post.objects.count()

class New(BaseView):
  def __init__(self, post, errors=None):
    super(New, self).__init__()
    self.post = post
    self.errors = errors

  def errors(self):
    if self.errors:
      return self.errors

class Edit(BaseView):
  def __init__(self, post, errors=None):
    super(Edit, self).__init__()
    self.post = post
    self.errors = errors

  def errors(self):
    if self.errors:
      return self.errors

class Show(BaseView):
  def __init__(self, post):
    super(Show, self).__init__()
    self.post = post

