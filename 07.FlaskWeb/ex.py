import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import map_util as mu  
import interpark_crawling as ic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ex.html')

@app.route('/scatter', methods=['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('ex_scatter.html')
    else:
        num = int(request.form['num'])
        mean = float(request.form['mean'])
        std = float(request.form['std'])
        max = int(request.form['max'])
        min = int(request.form['min'])
        xs = np.random.normal(loc=mean, scale=std, size=num)
        ys = np.random.uniform(low=min, high=max, size=num)
        plt.figure()
        plt.scatter(xs, ys)
        image_file = os.path.join(app.static_folder, 'img/scatter.png')
        plt.savefig(image_file)
        return render_template('ex_scatter_res.html')

@app.route('/hotplace', methods=['GET', 'POST'])
def hotplace():
    if request.method == 'GET':
        return render_template('ex_hotplace.html')
    else:
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        mu.hotplace(places, app) 
        return render_template('ex_hotplace_res.html')

@app.route('/interpark')
def interpark():
    lines = ic.crw()
    return render_template('ex_interpark.html', book_list=lines)

@app.route('/pb')
def pb():
    return render_template('ex_pb.html')

if __name__ == '__main__':
    app.run(debug=True)