from flask import Flask, render_template, request
import interpark_crawling as ic

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/interpark')
def interpark():
    lines = ic.crw()
    return render_template('11.interpark.html', book_list=lines)

if __name__ == '__main__':
    app.run(debug=True)