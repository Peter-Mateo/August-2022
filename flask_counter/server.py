from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "counter"


@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')

# Adds to the count
@app.route('/count', methods=['POST'])
def add():
    return redirect('/')

# Deletes the current session
@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.pop('counter', None)
    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)