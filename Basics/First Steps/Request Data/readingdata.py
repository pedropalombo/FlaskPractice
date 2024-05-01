#getting both Flask & request HTTP installed libs
from flask import Flask, request

app = Flask(__name__)

# ~ Testing POST method ~
# |-> go to testing client: 
#  \-> Body -> raw -> JSON -> set JSON to show
@app.route('/', methods=["POST"])
def index():
    #checking if data exists
    if request.data:
        #getting 'name' field based on JSON
        return _readData(request.get_json())
    else:
        return "hmmmmmmmmmmmm não"

#private function (_function) to read 'name' fields from sent data
# \-> OBS: fields are set in testing client (eg: Postman)  
def _readData(data):
    return data['name']

if __name__ == '__main__':
    app.run()