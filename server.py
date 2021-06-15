from flask import Flask, render_template, jsonify, request, redirect, \
                  send_from_directory
from trollfactory import generate, TROLLFACTORY_VERSION
from json import loads, dumps
from os.path import isfile
from uuid import uuid4
from subprocess import run
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tf_version=TROLLFACTORY_VERSION)

@app.route('/output', methods=['GET'])
def output():
    sex = request.args.get('sex')
    dataset = request.args.get('ds')
    while True:
        try:
            generated_person = generate(dataset, sex)
        except:
            pass
        if generated_person:
            break
    if request.args.get('output') == 'json':
        return jsonify(generated_person)
    else:
        person_uuid = str(uuid4())
        with open(''.join(['personalities/', person_uuid, '.json']), 'w') as file:
            file.write(dumps(generated_person))
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

@app.route('/del/<uuid:person_uuid>', methods=['POST'])
def delete_personality(person_uuid):
    file_paths = [
        ''.join(['personalities/', str(person_uuid), '.json']),
        ''.join(['personalities/', str(person_uuid), '.pdf'])
    ]
    if isfile(file_path):
        for file_path in file_paths:
            run(['shred', '-fuz', file_path])
    return redirect('/')

@app.route('/dl/<uuid:person_uuid>', methods=['GET'])
def download_personality(person_uuid):
    file_path = ''.join(['personalities/', str(person_uuid), '.json'])
    if isfile(file_path):
        return send_from_directory('personalities/',
                                    str(person_uuid) + '.json',
                                    as_attachment=True)
    return redirect('/')

@app.route('/api', methods=['GET'])
def api():
    return render_template('/api.html')

if __name__ == '__main__':
    app.run(port=2137)
