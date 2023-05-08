from flask import Flask, render_template, request
from weather_util import get_weather
import interpark_crawling as ic
import jini_module as jm
import siksin_module as sm

app = Flask(__name__)

@app.route('/')
def first():
    menu = {'ho':1, 'us':0, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app))

@app.route('/home')
def home():
    menu = {'ho':1, 'us':0, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app))

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':1, 'cr':0}
    return render_template('prototype/schedule.html', menu=menu, weather=get_weather(app))

@app.route('/selfi')
def selfi():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi.html', menu=menu, weather=get_weather(app))

@app.route('/selfi_food')
def selfi_food():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi_food.html', weather=get_weather(app), menu=menu)

@app.route('/selfi_hobby')
def selfi_hobby():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi_hobby.html', weather=get_weather(app), menu=menu)

@app.route('/selfi_travel')
def selfi_travel():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi_travel.html', weather=get_weather(app), menu=menu)

@app.route('/interpark')
def interpark():
    lines = ic.crw()
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':0, 'cr':1}
    return render_template('prototype/interpark.html', weather=get_weather(app), menu=menu, book_list=lines)

@app.route('/jini')
def jini():
    jini_list = jm.jini()
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':0, 'cr':1}
    return render_template('prototype/jini.html', weather=get_weather(app), menu=menu, jini_list=jini_list)

@app.route('/siksin')
def siksin():
    food_list = sm.siksin()
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':0, 'cr':1}
    return render_template('prototype/siksin.html', weather=get_weather(app), menu=menu, food_list=food_list)

if __name__ == '__main__':
    app.run(debug=True)