import bottle, config.settings as s
from bottle import route, run, request, response, send_file, abort, redirect
from views.posts import Index, New, Show
from models.post import Post

@route('/')
def posts_index():
  return Index().render()

@route('/posts', method='POST')
def posts_create():
  Post.save(request.POST)
  redirect('/', 301)

@route('/posts/:id')
def posts_show(id):
  post = Post.find_one(id)
  if post:
    return Show(post).render()
  else:
    abort(404, 'Not found')

@route('/posts/new')
def posts_new():
  return New().render()

@route('/posts/:id', method='DELETE')
def posts_delete(id):
  post = Post.remove(id)

@route('/static/:filename#.*#')
def static_file(filename):
    send_file(filename, root='static')

bottle.debug(True)

run(host=s.host, port=s.port, reloader=s.reloader)
