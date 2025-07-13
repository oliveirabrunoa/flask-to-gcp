from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'This is your web app! Let\'s get going!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
