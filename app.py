from flask import Flask, render_template, flash, redirect, session, request
import os
import sqlite3


from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import *

app = Flask(__name__)

gastos_compartidos = []


DATABASE = 'fairfriends.db'

@app.route('/')
@login_required
def index():
    return render_template('index.html', gastos=gastos_compartidos)

@app.route('/agregar_gasto', methods=['POST'])
@login_required
def agregar_gasto():
    concepto = request.form['concepto']
    ponedor = request.form['ponedor']
    monto = float(request.form['monto'])


    # Agregar el nuevo gasto a la lista
    gastos_compartidos.append({'concepto': concepto, 'persona':ponedor, 'monto': monto})
    return render_template('montos.html', gastos=gastos_compartidos)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Ensure username was submitted
        """
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation") == request.form.get("password"):
            return apology("Your password don't match", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) >= 1:
            return apology("invalid username it already exist", 400)

        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password")),
        )
        
        # Remember which user has logged in
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        """
        return redirect("/")

    elif request.method == "GET":
        return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    #session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        """
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        """
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)
