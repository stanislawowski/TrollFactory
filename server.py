from flask import Flask, render_template, jsonify, request
from trollfactory import generate
from json import loads
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output', methods=['GET'])
def output():
    sex = request.args.get('sex')
    lang = request.args.get('lang')
    if request.args.get('output') == 'json':
        return jsonify(generate(lang, sex))
    else:
        return render_template('/output.html', generated=loads(generate(lang, sex)))

if __name__ == '__main__':
    app.run(port=2137)
