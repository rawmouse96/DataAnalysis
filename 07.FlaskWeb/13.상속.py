from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/bootstrap')
def bootstrap():
    return render_template('13.bootstrap.html')

@app.route('/carousel')
def carousel():
    return render_template('13.carousel.html')

@app.route('/pb')
def pb():
    return render_template('13.progressbar.html')

if __name__ == '__main__':
    app.run(debug=True)