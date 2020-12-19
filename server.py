from flask import Flask, render_template
from trollfactory import generate
from json import loads
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output/<language>/<sex>')
def output(language, sex):
	generated = loads(generate(language, sex))
	return render_template('/output.html', generated=generated)

@app.route('/json/<language>/<sex>')
def json(language, sex):
    return generate(language, sex)

if __name__ == '__main__':
    app.run(port=2137)
