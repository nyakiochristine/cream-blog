from flask import render_template
from . import main


@main.errorhandler(404)
def error():
    return render_template('/404.html')

@main.errorhandler(403)
def error():
    return render_template('/403.html')


@main.errorhandler(500)
def error():
    return render_template('/500.html')

