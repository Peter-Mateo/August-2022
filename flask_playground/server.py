from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html')

@app.route('/play/<times>')
def play(times):
    return render_template('next_step.html', times=int(times))

@app.route('/play/<times>/<color>')
def play_color(times, color):
    return render_template('last_step.html', times=int(times), color=color)

if __name__ == '__main__':
    app.run(debug=True)