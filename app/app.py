from flask import Flask, jsonify, render_template
from os import environ
from core import util

app = Flask(__name__, static_url_path='/static', template_folder='template')
appmode = environ.get('FLASKMODE', '')

# diffrent ports on server and local
PORT = 80 if appmode == 'server' else 5000

@app.route('/')
def index():
    return render_template('index.html', mode=appmode)

@app.route('/ajax')
def ajax():
    res = util.shapeshift(['1234X5786', '12345X786', '12345678X'])
    return jsonify({'data': res})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)

