from flask import Flask, render_template, request
from weather_util import get_weather
from weather_util import get_weather2
import interpark_crawling as ic
import jini_module as jm
import siksin_module as sm
import os, random
import img_util as iu

app = Flask(__name__)

# for AJAX ######################################################
@app.before_first_request
def before_first_request():
    global quote, quotes # quote/quotes to global variance
    global addr
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as f:
        quotes = f.readlines()
    quote = random.sample(quotes, 1)[0]
    addr = '수원시 장안구'
    
@app.route('/change_profile', methods=['POST'])
def change_profile():
    file_image = request.files['image']
    filename = os.path.join(app.static_folder, f'upload/{file_image.filename}')
    file_image.save(filename)
    iu.change_profile(app, filename)
    return ''
    
@app.route('/change_quote')
def change_quote():
    global quote
    quote = random.sample(quotes, 1)[0]
    return quote

@app.route('/change_addr')
def change_addr():
    global addr
    addr = request.args.get('addr')
    return addr

@app.route('/weather')
def weather():
    global weather2
    addr = request.values['addr']
    weather2 = get_weather2(app, addr)
    return weather2
###################################################################
@app.route('/')
def first():
    menu = {'ho':1, 'us':0, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/base.html', menu=menu, weather=get_weather(app), quote = quote, addr=addr)

@app.route('/home')
def home():
    menu = {'ho':1, 'us':0, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app), quote = quote, addr=addr)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':1, 'cr':0}
    return render_template('prototype/schedule.html', menu=menu, weather=get_weather(app), quote = quote, addr=addr)

@app.route('/selfi')
def selfi():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi.html', menu=menu, weather=get_weather(app), quote = quote, addr=addr)

@app.route('/selfi_food')
def selfi_food():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi_food.html', weather=get_weather(app), menu=menu, quote = quote, addr=addr)

@app.route('/selfi_hobby')
def selfi_hobby():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi_hobby.html', weather=get_weather(app), menu=menu, quote = quote, addr=addr)

@app.route('/selfi_travel')
def selfi_travel():
    menu = {'ho':0, 'us':1, 'ai':0, 'sc':0, 'cr':0}
    return render_template('prototype/selfi_travel.html', weather=get_weather(app), menu=menu, quote = quote, addr=addr)

@app.route('/interpark')
def interpark():
    lines = ic.crw()
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':0, 'cr':1}
    return render_template('prototype/interpark.html', weather=get_weather(app), menu=menu, book_list=lines, quote = quote, addr=addr)

@app.route('/jini')
def jini():
    jini_list = jm.jini()
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':0, 'cr':1}
    return render_template('prototype/jini.html', weather=get_weather(app), menu=menu, jini_list=jini_list, quote = quote, addr=addr)

@app.route('/siksin')
def siksin():
    food_list = sm.siksin()
    menu = {'ho':0, 'us':0, 'ai':0, 'sc':0, 'cr':1}
    return render_template('prototype/siksin.html', weather=get_weather(app), menu=menu, food_list=food_list, quote = quote, addr=addr)

if __name__ == '__main__':
    app.run(debug=True)