from flask import Flask 
from flask import Blueprint, render_template
bars = Blueprint(__name__, "bars")

@bars.route("/")
def map():
    return render_template("Bars.html")