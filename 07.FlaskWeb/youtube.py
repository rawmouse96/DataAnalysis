from flask import Flask, render_template, request
import youtube_module as ym
app = Flask(__name__)

@app.route('/youtube_ranking')
def melon():
    lines, cat_cnt, df1 = ym.youtube()
    return render_template('/youtube.html', df1=df1, cat_cnt=cat_cnt)

if __name__ == '__main__':
    app.run(debug=True)