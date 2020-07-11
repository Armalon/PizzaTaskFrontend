from flask import Flask, escape, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World') # this is context local https://flask.palletsprojects.com/en/1.1.x/quickstart/#context-locals
    username = 'usermy'
    link_address = url_for('show_user_profile', username=username)
    static_link = url_for('static', filename='style.css')
    return f'Hello!, {escape(name)}. Here is the link to <a href="{link_address}">{username}</a> <br> and here is s just <a href="{static_link}">link</a>'

@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    return render_template('hello.html', username=username)

@app.route('/test')
def test():
    return 'Test page'


