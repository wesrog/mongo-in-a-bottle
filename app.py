import bottle, config.settings as s
import mongoengine
from bottle import route, run, request, response, send_file, abort, redirect
from views.posts import Index, New, Edit, Show
from models.post import Post

@route('/')
def posts_index():
  return Index().render()

@route('/posts/new')
def posts_new():
  post = Post()
  return New(post).render()

@route('/posts', method='POST')
def posts_create():
  post = Post()
  for k in request.POST:
    if request.POST[k] == '':
      post.__setitem__(k, None)
    else:
      post.__setitem__(k, request.POST[k])

  try:
    post.validate()
    post.save()
    redirect('/')
  except mongoengine.ValidationError, e:
    return New(post, e).render()

@route('/posts/:id')
def posts_show(id):
  post = Post.objects.get(id=id)
  if not post:
    abort(404, 'Not found')

  return Show(post).render()

@route('/posts/:id/edit')
def posts_edit(id):
  post = Post.objects.get(id=id)
  if post:
    return Edit(post).render()
  else:
    abort(404, 'Not found')

@route('/posts/:id', method='POST')
def posts_update(id):
  post = Post.objects.get(id=id)
  if not post:
    abort(404, 'Not found')

  #post.save(request.POST)
  for k in request.POST:
    if request.POST[k] == '':
      post.__setitem__(k, None)
    else:
      post.__setitem__(k, request.POST[k])

  try:
    post.validate()
    post.save()
    redirect('/')
  except mongoengine.ValidationError, e:
    return Edit(post, e).render()

@route('/posts/:id', method='DELETE')
def posts_delete(id):
  p = Post.objects.get(id=id)
  p.delete()

@route('/static/:filename#.*#')
def static_file(filename):
    send_file(filename, root='static')

bottle.debug(s.debug)

run(host=s.host, port=s.port, reloader=s.reloader)
