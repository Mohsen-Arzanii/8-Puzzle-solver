from flask import Flask, jsonify
from core import util

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/ajax')
def ajax():
    res = util.shapeshift(['1234X5786', '12345X786', '12345678X'])
    return jsonify({'data': res})

if __name__ == '__main__':
    app.run()
