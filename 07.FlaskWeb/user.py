from flask import Blueprint, request, render_template, session, redirect, flash
import hashlib, base64, json

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['GET', 'POST'])        # localhost:5000/user/login이 처리되는 곳
def login():
    if request.method == 'GET':
        menu = {'ho':0, 'us':0, 'ai':0, 'sc':0, 'cr':0}
        return render_template('prototype/user/login.html', menu=menu)
    else:
        with open('static/data/password.txt') as f:
            s = f.read()
        passwords = json.loads(s)    
        uid = request.form['uid']
        pwd = request.form['pwd']
        if uid in passwords.keys():
            pwd_sha256 = hashlib.sha256(pwd.encode())
            hashed_pwd = base64.b64encode(pwd_sha256.digest()).decode('utf-8')
            if hashed_pwd == passwords[uid]:
                flash('환영합니다.') 
                session['uid']=uid
                return redirect('/')
            else:
                flash('비밀번호 오류')
                return redirect('/user/login')
        else:
            flash('id가 잘못됨')
            return redirect('/user/register')

@user_bp.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect('/')

@user_bp.route('/register')
def register():
    return render_template('prototype/user/register.html')