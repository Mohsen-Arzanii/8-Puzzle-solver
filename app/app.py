from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from os import environ
from model import Puzzle
from core import util, ids, astar

app = Flask(__name__, static_url_path='/static', template_folder='template')
CORS(app) # enable cors
appmode = environ.get('FLASKMODE', '')

# diffrent ports on server and local
PORT = 80 if appmode == 'server' else 5000

@app.route('/')
def index():
    return render_template('index.html', mode=appmode)

@app.route('/ajax', methods=['POST'])
def ajax():
    DEFAULT_STATE = Puzzle('12345678X')
    solvable = num_of_nodes = path = None

    data = request.get_json()
    approach = data.get('approach', None)
    state = Puzzle(data.get('state', DEFAULT_STATE))

    # select the correct approach
    solvable, num_of_nodes, path = astar(state) if approach == 'astar' else ids(state)

    result = util.shapeshift(path) if solvable else None
    return jsonify({'solvable': solvable, 'level': len(result), 
        'num_of_nodes': num_of_nodes, 'data': result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)

