from flask import Flask, render_template
from trollfactory import generate_web
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output/<language>/<sex>')
def output(language, sex):
	generated = generate_web(language, sex, 'normal')
	return render_template('/output.html', generated=generated)

@app.route('/json/<language>/<sex>')
def json(language, sex):
    return generate_web(language, sex, 'json')

if __name__ == '__main__':
    app.run(port=2137)
