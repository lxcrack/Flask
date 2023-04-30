from flask import  Blueprint, render_template, request, flash

views = Blueprint('views', __name__)
@views.route('/')
@views.route('/index.html')
def home():
    return render_template("index.html")
    
