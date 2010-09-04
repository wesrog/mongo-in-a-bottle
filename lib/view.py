import pystache
from models.post import Post

class BaseView(pystache.View):
  def __init__(self):
    self.view_name = self.__class__.__name__
    self.template_path = 'templates/%s' % self.view_name

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

