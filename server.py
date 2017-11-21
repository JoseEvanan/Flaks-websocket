from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True
@app.route('/')
def index():
    print("index")
    return render_template('index.html')

@app.route('/api')
def api():
    print("api")
    if request.environ.get('wsgi.websocket'):
        print("1")
        ws = request.environ['wsgi.websocket']
        print("2")
        while True:
            message = ws.receive()
            print("message ", message)
            ws.send(message)
    return

if __name__ == '__main__':
    http_server = WSGIServer(('',5000), app,
                             handler_class=WebSocketHandler)
    http_server.serve_forever()
