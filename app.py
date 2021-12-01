from flask import Flask, render_template, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/private/mystall', methods=['POST'])
def mystall():
    return Response(request.get_json(), status=200)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
