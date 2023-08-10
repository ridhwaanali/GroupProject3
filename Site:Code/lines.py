from flask import Flask 
from flask import Blueprint, render_template
lines = Blueprint(__name__, "lines")

@lines.route("/")
def map():
    return render_template("lines.html")
