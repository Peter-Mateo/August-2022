from app import app
@app.route('/')
def index():
    return "you did it"