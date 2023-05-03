from flask import Flask, render_template, request
import pandas as pd
from urllib.parse import quote
import map_util as mu

app = Flask(__name__)

@app.route('/hotplace', methods=['GET', 'POST'])
def hotplace():
    if request.method == 'GET':
        return render_template('10.수원HotPlace.html')
    else:
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        
        mu.hotplace(places, app) 
        
        return render_template('10.수원HotPlace_res.html')
        
if __name__ == '__main__':
    app.run(debug=True)