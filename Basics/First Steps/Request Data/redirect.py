# getting both Flask and Request libs, as well as Flask's methods
from flask import Flask, request, redirect, url_for, abort

app = Flask(__name__)

# =| Routing |=

# ~ Index ~
@app.route('/', methods=["GET"])
def index():
    return ""

# ~ Profile ~
# \-> OBS: parameters on URL <=> function
@app.route('/<name>/<password>')
def readData(name, password):
    if (name == 'admin' and password == 'admin'):
        return redirect(url_for('admin'))
    
    #throwing "Unathorized" error to client
    else:
        abort(401) 
    
# ~ Admin ~
@app.route('/admin')
def admin():
    return "This is from the admin dashboard."

if __name__ == '__main__':
    app.run()