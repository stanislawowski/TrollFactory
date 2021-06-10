from flask import Flask, render_template, jsonify, request
from trollfactory import generate, TROLLFACTORY_VERSION
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tf_version=TROLLFACTORY_VERSION)

@app.route('/output', methods=['GET'])
def output():
    sex = request.args.get('sex')
    dataset = request.args.get('ds')
    if request.args.get('output') == 'json':
        return jsonify(generate(dataset, sex))
    else:
        return render_template('/output.html', generated=generate(dataset, sex))

@app.route('/api', methods=['GET'])
def api():
    return render_template('/api.html')

if __name__ == '__main__':
    app.run(port=2137)
