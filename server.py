from flask import Flask, render_template, jsonify, request, redirect
from trollfactory import generate, TROLLFACTORY_VERSION
from json import loads, dumps
from os.path import isfile
from uuid import uuid4
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
        person_uuid = str(uuid4())
        with open(''.join(['personalities/', person_uuid, '.json']), 'w') as file:
            file.write(dumps(generate(dataset, sex)))
        return redirect(f'/{person_uuid}')

@app.route('/<uuid:person_uuid>', methods=['GET'])
def output_uuid(person_uuid):
    file_path = ''.join(['personalities/', str(person_uuid), '.json'])
    if isfile(file_path):
        return render_template('/output.html', 
                               generated = loads(open(file_path).read()),
                               id = person_uuid)
    else:
        return redirect('/')

@app.route('/api', methods=['GET'])
def api():
    return render_template('/api.html')

if __name__ == '__main__':
    app.run(port=2137)
