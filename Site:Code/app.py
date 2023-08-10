from flask import Flask, render_template 
from lines import lines
from scatters import scatters
from bars import bars

app= Flask(__name__, template_folder= 'Templates')
@app.route("/")
def home():
    return render_template("Home.html")


app.register_blueprint(lines, url_prefix="/lines")
app.register_blueprint(scatters, url_prefix="/scatters")
app.register_blueprint(bars, url_prefix="/Bars")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

