from flask import Flask, render_template, request, flash, redirect
import db.kpop_dao as kd

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask with MySQL'

@app.route('/song/list')
def song_list():
    if request.method == 'GET':
        songs = kd.get_song_list(20)
        return render_template('01.song_list.html', songs=songs)
    else:
        title = request.form["title"]
        lyrics = request.form["lyrics"]
        params = (title, lyrics)
        kd.insert_song(params)
        flash('추가되었습니다.')
        return redirect('/')

@app.route('/gg/list')
def gg_list():
    groups = kd.get_girl_group_list(20)
    return render_template('11.gg_list.html', groups=groups)

if __name__ == '__main__':
    app.run(debug=True)