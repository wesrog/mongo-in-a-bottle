import bottle
from bottle import route, run, request, response, send_file, abort, redirect
import views as v
from views.posts import Index, Show
from models.post import Post

@route('/', method='GET')
def posts_index():
    return Index().render()

@route('/posts', method='POST')
def posts_create():
  if not request.POST['author'] == '':
    v.posts.posts.insert(request.POST) # ugly!
  redirect('/')

@route('/posts/:id')
def posts_show(id):
  post = Post.find_one(id)
  s = Show()
  s.post = post
  return s.render()

@route('/posts/:id', method='DELETE')
def posts_delete(id):
  post = Post.remove(id)

@route('/hello/:name')
def hello_name(name):
    return 'Hello %s!' % name

@route('/hello', method='POST')
def hello_post():
    name = request.POST['name']
    return 'Hello %s!' % name

@route('/static/:filename#.*#')
def static_file(filename):
    send_file(filename, root='static')

@route('/template/test')
def template_test():
    return template('template_name', title='Template Test', items=[1,2,3,'fly'])

bottle.debug(True)

run(host='localhost', port=3000, reloader=True)
