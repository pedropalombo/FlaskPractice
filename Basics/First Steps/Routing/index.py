#first steps are to:
#-> install virtualenv for isolated projects
 # \-> pip install virtualenv
#-> create enviroment
 # \-> virtualenv project-name
#-> activate the virtual environment
 # \-> directory\Scripts\activate
#-> intall flask
 # \-> pip install flask

#importing Flask's lib
from flask import Flask

#setting Flask's nametag
app = Flask(__name__)

#preparing Routing for index
# \-> @app.route('/route-name, methods=[ALLOWED_METHODS])
# \-> def functionName():
    # \-> return "Message/HTML", statusCode
@app.route('/', methods=["GET"])
def index():
    return "Ayo, it's on!", 200

#setting "getname" route, as well as return type
@app.route('/getname', methods=["GET"])
def getName() -> str:
    return 'name of yours'

#setting dynamic routing and getting the value through URL
# \-> PS: parameter must be the same as <variableName> tag name
@app.route('/name/<yourName>', methods=["GET"])
def name(yourName):
    return 'Hello %s' % yourName

# '', enforcing the type of the variable, and changing the status code shown
@app.route('/age/<int:age>', methods=["GET"])
def getAge(age):
    return 'Your age is %d' % age, 500

#if Flask's name is 'main', then it runs the server
if __name__ == '__main__':
    app.run(port=5500) #running app on specific port
