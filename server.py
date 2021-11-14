from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'S_Key'

@app.route('/')
def home():
    if 'visit_counter' in session:
        print('good')
        session['visit_counter'] = session['visit_counter'] + 1
    else:
        session['visit_counter'] = 0
        print('bad')
    return render_template('counter.html')

@app.route('/count')
def counter():
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)