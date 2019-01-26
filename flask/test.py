from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    return "it verkskskksksksksssss"

if __name__ == '__main__':
    app.run(host='172.17.99.57', debug=True, port=3134)