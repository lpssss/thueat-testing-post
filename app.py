import json
from flask import Flask, render_template, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/private/mystall/dishes', methods=['POST'])
def mystall_dishes():
    obj={"foo":"bar", "foo1":"bar1"}
    return Response(json.dumps(obj), status=200, mimetype='application/json')

@app.route('/private/mystall', methods=['POST'])
def mystall():
    print(request.get_json(),flush=True)
    return Response(request.json, status=200, mimetype='application/json')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
