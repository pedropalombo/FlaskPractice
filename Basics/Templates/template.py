from flask import Flask, render_template

app = Flask(__name__)

# =| Routing |=

# ~ Index ~
@app.route('/', methods=["GET"])
def index():
    #returning template file
    return render_template('index.html')


# ~ Dashboard ~
# sending vars to other files
@app.route('/dashboard/<name>', methods=["GET"])
def dashboard(name):
    #rendering file and sending 'userName' to the HTML document
    return render_template('dashboard.html', userName=name)

# ~ Error ~
@app.route('/error', methods=["GET"])
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()