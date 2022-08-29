from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "survey"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/process', methods=['POST'])
def process():
    print("Processed")
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    return redirect('/results')

if __name__ == '__main__':
    app.run(debug=True)