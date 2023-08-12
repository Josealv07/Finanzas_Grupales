import csv
import datetime
import subprocess
import urllib
import uuid
import locale

from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400):
    def escape(s):
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function




def format_money(amount):
    # Establecer la localización a Colombia
    locale.setlocale(locale.LC_ALL, 'es_CO.utf8')

    # Formatear el monto en dinero colombiano
    formatted_money = locale.currency(amount, grouping=True, symbol=True)

    return formatted_money
