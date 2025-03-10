#FROM GABE
import json
from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)
@app.route('/', methods=['POST'])
def log():
    data = json.loads(request.data)
    print(data)
    return ''

# create a log.py file on the controller server with the above. Then run it with the command below. 
# If flask is not installed, use pip3 to install.
   # pip3 install flask --user
# FLASK_APP=log flask run -h 0.0.0.0 -p 8080


#------------------------------------------------------------------------------------------------#
# FROM BEN
import json
from flask import Flask, escape, request
from markupsafe import escape
import logging
app = Flask(__name__)
logging.basicConfig(filename='tower_elk.log', level=logging.DEBUG)
@app.route('/', methods=['POST'])
def log():
    data = json.loads(request.data)
    print(data)
    return ''

# create a log.py file on the controller server with the above. Then run it with the command below. 
# If flask is not installed, use pip3 to install.
   # pip3 install flask --user
# FLASK_APP=log flask run -h 0.0.0.0 -p 8080


#-------------------------------------------------------------------------#
#Controller settings:
#Logging Aggregator = http://localhost
#Logging Aggregator Port = 8080
#Logging Aggregator Type = Other
#Logging Aggregator Protocol = HTTPS/HHTP
#
#













