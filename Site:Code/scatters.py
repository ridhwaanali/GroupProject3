from flask import Flask 
from flask import Blueprint, render_template
scatters = Blueprint(__name__, "scatters")

@scatters.route("/")
def map():
    return render_template("scatters.html")
