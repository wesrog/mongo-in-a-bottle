import bottle, config.settings as s
from bottle import route, run, request, response, send_file, abort, redirect
from views.posts import Index, New, Show, Edit
from models.post import Post

@route('/')
def posts_index():
  return Index().render()

@route('/posts', method='POST')
def posts_create():
  post = Post(request.POST)
  post.save()
  redirect('/', 301)

@route('/posts/:id')
def posts_show(id):
  post = Post.find_one(id)
  if post:
    return Show(post).render()
  else:
    abort(404, 'Not found')

@route('/posts/:id/edit')
def posts_edit(id):
  post = Post.find_one(id)
  if post:
    return Edit(post).render()
  else:
    abort(404, 'Not found')

@route('/posts/:id', method='POST')
def posts_update(id):
  post = Post.find_one(id)
  if post:
    post.save(request.POST)
    redirect('/', 301)
  else:
    abort(404, 'Not found')

@route('/posts/new')
def posts_new():
  return New().render()

@route('/posts/:id', method='DELETE')
def posts_delete(id):
  p = Post.find_one(id)
  p.remove()

@route('/static/:filename#.*#')
def static_file(filename):
    send_file(filename, root='static')

bottle.debug(s.debug)

run(host=s.host, port=s.port, reloader=s.reloader)
