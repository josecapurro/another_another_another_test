# uwsgi requires the WSGI entry point to be named "application"
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hell-o World!']
