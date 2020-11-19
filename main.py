from flask import Flask, render_template, request, redirect, url_for
from replit import db
import time

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def form():
  if request.method == "POST":
    db[request.form['seat']] = request.form['status']
    return redirect(url_for('queue'))
  else:
    return render_template('form.html')

@app.route("/queue", methods=["GET","POST"])
def queue():
  if request.method == "POST":
    for i in range(1,29):
      db[i] = ""
    return render_template('queue.html', seats=db)
  else:
    return render_template('queue.html', seats=db)





app.run("0.0.0.0")