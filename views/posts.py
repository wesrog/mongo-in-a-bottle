import os
import pystache
from models.post import Post

#view_name = os.path.basename(__file__).split('.')[0]
view_name = 'posts'
model_name = 'post'
model = globals()[model_name.capitalize()]

class BaseView(pystache.View):
  template_path = 'templates/%s' % view_name

  def __getattr__(self, name):
    try:
      if name in self.__getattribute__(model_name).data:
        return self.__getattribute__(model_name).data[name]
      else:
        return self.__getattribute__(model_name).__getattribute__(name)()
    except:
      AttributeError

def posts(self):
  return not empty(self)

def empty(self):
  return len(model.all()) == 0

def post(self):
  posts = model.all()
  for p in posts:
    p.data['untitled'] = p.untitled()
    p.data['anonymous'] = p.anonymous()
    p.data['url'] = p.url()
  return [p.data for p in posts]

setattr(BaseView, view_name, posts)
setattr(BaseView, 'empty', empty)
setattr(BaseView, 'post', post)

class Index(BaseView):
  pass

class New(BaseView):
  def post(self):
    return model

class Edit(BaseView):
  def __init__(self, post):
    super(Edit, self).__init__()
    self.post = model(post.data)

class Show(BaseView):
  def __init__(self, post):
    super(Show, self).__init__()
    self.post = model(post.data)
