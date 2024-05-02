from flask import Flask, render_template

app = Flask(__name__)

# =| Routing |=

# ~ Index ~
# testing out Errors and Exceptions
@app.route('/')
def index():
    # -> Using Try/Catch
    '''try:
        12/0 #returning a value that's divided by 0

    # throwing generic Exception and getting the error type
    except Exception as e:
        return "Some server error happened, which was this:\n %s" % e.__class__.__name__
    '''
    # -> Using ErrorHandlers
    return "just a sample text" + 43

# setting a server-side error handler
@app.errorhandler(500)
def serverError(error):
    #returning specific HTML to be shown when the error is triggered
    return render_template("error_demo.html")


if __name__ == '__main__':
    app.run()