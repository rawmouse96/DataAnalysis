# 점의 갯수 100, 200
# X: 정규분포, 평균, 표준편차, Y: 균등분포, 최소, 최대

import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'main'

@app.route('/scatter', methods=['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('09.산점도.html')
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
        return render_template('09.산점도_res.html')
        
if __name__ == '__main__':
    app.run(debug=True)