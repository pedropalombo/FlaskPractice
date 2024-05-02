from flask import Flask, render_template

#importing SQLite
import sqlite3

app = Flask(__name__)

# =| Routing |=

# ~ Index ~
@app.route("/")
def index():
    # creating/connecting to the db
    connection = sqlite3.connect("students.db")

    # setting a table on the db
    connection.execute('CREATE TABLE student(name text)')

    #returning the confirmation page
    return render_template('content.html', msg="Database and its tables have been created!")

# ~ Insert ~
@app.route("/insert")
def createRecord():

    # name to be added to the db
    name = 'Pietrus'

    # using the created db ...
    with sqlite3.connect("students.db") as conn:

        # ... and setting a cursor to it ...
        # \-> OBS: used for data retrieval
        cur = conn.cursor()

        # ... we can now insert a value into the created table
        # \-> PS: values to be accessed must always be surrounded by []
        cur.execute("INSERT INTO student (name) VALUES (?)", [name])

        # saving changes
        conn.commit()

        # closing the cursor
        cur.close()

    # rendering the confirmation page
    return render_template('content.html', msg="Values inserted successfully!")


# ~ Dynamic ~
# getting the values to be inserted into db through URL
@app.route('/dynamic/<text>')
def dynamic_record(text):
    name = text

    with sqlite3.connect("students.db") as conn:
        cur = conn.cursor()

        cur.execute("INSERT INTO student (name) VALUES (?)",  [name])

        conn.commit()

        cur.close()
    
    return render_template('content.html', msg="Dynamic value acquired and saved!")


# ~ Select ~
# displaying info from DB
@app.route("/select")
def selectAllRecords():

    #stabilishing connectiong to DB
    with sqlite3.connect("students.db") as conn:
        
        # getting all rows from db in a "Row" format
        conn.row_factory = sqlite3.Row

        # setting the cursor
        cur = conn.cursor()

        # adding all rows to the cursor
        cur.execute("SELECT * FROM student")

        # copying everything inside it to a var ...
        rows = cur.fetchall()

        # ... so we can close the cursor
        cur.close()

    # sending the info over to the HTML page
    # \-> OBS: using a different template so I don't lose on the example for the 'msg'
    return render_template('db_contents.html', tableRows = rows) 


if __name__ == '__main__':
    app.run()