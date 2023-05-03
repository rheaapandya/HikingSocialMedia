from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "Change Me"

# TODO: Fill in methods and routes
@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")
@app.route("/gethiking")
def gethiking():
    return render_template("gethiking.html")
@app.route("/youradventuresofar")
def youradventuresofar():
    return render_template("youradventuresofar.html")
@app.route("/login")
def login():
    return render_template("login.html")



@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
