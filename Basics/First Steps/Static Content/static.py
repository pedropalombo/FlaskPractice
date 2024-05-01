#importing Flask and render_template
# \-> "render_template" renders HTML pages
# \-> PS: it doesn't support comments 
from flask import Flask, render_template

#setting it's tag name
app = Flask(__name__)

# =| Routing |=

# ~ Index ~
@app.route('/', methods=["GET"])
def index():
    return "Static content application"

# ~ Static Page ~
# printing the HTML page as a response
@app.route('/static')
def static_method():
    return render_template('static.html')

# running the app
if __name__ == '__main__':
    app.run()