#importing libraries 
import json
from flask import flask 
from map import map 
from scatter import scatter
from line import line

#importing and reading json
f=  open('final.json')
data= json.load(f)
for i in data['emp_details']:
    print (i)
    f.close()

#creating flask app
app= Flask(__name__)
@app.route("/")

def home():
    return render_template("Home.html")
app.register_blueprint(map, url_prefix="/map")
app.register_blueprint(map, url_prefix="/scatter")
app.register_blueprint(map, url_prefix="/line")

if __name__ --'__main__':
    app.run(debug=True, port=8000)
    