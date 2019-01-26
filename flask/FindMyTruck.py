from flask import Flask, request
app = Flask(__name__)

@app.route('/gpsdata')
def query():
    return

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        beginlat = request.form.get('beginlat')
        beginlong = request.form.get('beginlong')
        endlat = request.form.get('endlat')
        endlong = request.form.get('endlong')
        weight = request.form.get('weight')
        return '''<h1>[{},{},{},{},{}]</h1>'''.format(beginlat,beginlong,endlat,endlong,weight)
    
    return '''<form method="POST">
                beginlat: <input type="text" name="beginlat"><br>
                beginlong: <input type="text" name="beginlong"><br>
                endlat: <input type="text" name="endlat"><br>
                endlong: <input type="text" name="endlong"><br>
                weight: <input type="text" name="weight"><br>  
                <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/')
def display():
    return "hello"

if __name__ == '__main__':
    app.run(host='172.17.99.57', debug=True, port=3134)