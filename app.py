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


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        username = request.form["username"]
        firstpassword = request.form["password"]
        secondpassword = request.form["repassword"]
        if (firstpassword == secondpassword) and (db_session.query(User).where(username == User.username).first() == None):
            new_user = User(username=username, password=firstpassword)
            db_session.add(new_user)
            db_session.commit()
            session["username"] = username
            return redirect(url_for("youradventuresofar", username=username))
        else:
            flash("Username Already Taken or Passwords Don't Match", "info")
            return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        if db_session.query(User).where((username == User.username) & (password == User.password)).first() == None:
            flash("Invalid Password or Username", "info")
            return render_template("login.html")
        else:
            return redirect(url_for("youradventuresofar", username=session["username"]))


@app.route("/youradventuresofar")
def youradventuresofar():
    if "username" not in session:
        flash("Sign in to view", "info")
        return redirect(url_for("signup"))
    else:
        userhike1 = db_session.query(Userhike).where(
            Userhike.user_id == session["username"]).first()
        if userhike1 == None:
            userhike1 = "Do more hikes to fill this out!"
            userhike2 = "Do more hikes to fill this out!"
            userhike3 = "Do more hikes to fill this out!"
            userhike4 = "Do more hikes to fill this out!"
        else:
            hikeid = userhike1.hike_id
            userhike1 = db_session.query(Hike).where(
                Hike.id == hikeid).first().name
            userhike2 = db_session.query(Userhike).where(
                Userhike.user_id == session["username"]).limit(1).offset(1).first()
            if userhike2 == None:
                userhike2 = "Do more hikes to fill this out!"
                userhike3 = "Do more hikes to fill this out!"
                userhike4 = "Do more hikes to fill this out!"
            else:
                hikeid = userhike2.hike_id
                userhike2 = db_session.query(Hike).where(
                    Hike.id == hikeid).first().name
                userhike3 = db_session.query(Userhike).where(
                    Userhike.user_id == session["username"]).limit(1).offset(2).first()
                if userhike3 == None:
                    userhike3 = "Do more hikes to fill this out!"
                    userhike4 = "Do more hikes to fill this out!"
                else:
                    hikeid = userhike3.hike_id
                    userhike3 = db_session.query(Hike).where(
                        Hike.id == hikeid).first().name
                    userhike4 = db_session.query(Userhike).where(
                        Userhike.user_id == session["username"]).limit(1).offset(3).first()
                    if userhike4 == None:
                        userhike4 = "Do more hikes to fill this out!"
                    else:
                        hikeid = userhike4.hike_id
                        userhike4 = db_session.query(Hike).where(
                            Hike.id == hikeid).first().name

        return render_template("youradventuresofar.html", user=session["username"], hike1=userhike1, hike2=userhike2, hike3=userhike3, hike4=userhike4)


@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
    return render_template("index.html")


@app.route("/windyhill")
def windyhill():
    return render_template("windyhill.html")


@app.route("/montara")
def montara():
    return render_template("montara.html")


@app.route("/dish")
def dish():
    return render_template("dish.html")


@app.route("/almaden")
def almaden():
    return render_template("almaden.html")


@app.route("/santateresa")
def santateresa():
    return render_template("santateresa.html")


@app.route("/sequoia")
def sequoia():
    return render_template("sequoia.html")


@app.route("/berry")
def berry():
    return render_template("berry.html")


@app.route("/blackmountain")
def blackmountain():
    return render_template("blackmountain.html")


@app.route("/mission")
def mission():
    return render_template("mission.html")


@app.route("/saratoga")
def saratoga():
    return render_template("saratoga.html")


@app.route("/russianridge")
def russianridge():
    return render_template("russianridge.html")


@app.route("/purisma")
def purisma():
    return render_template("purisma.html")


@app.route("/addwindy")
def addwindy():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Windy Hill Loop").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addalmaden")
def addalmaden():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Almaden Lake").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addbmountain")
def addbmountain():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Black Mountain Trail").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addberry")
def addberry():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Berry Creek Falls Loop").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/adddish")
def adddish():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Stanford Dish Loop Trail").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addmission")
def addmission():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Mission Peak Loop").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addmontara")
def addmontara():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Montara Mountain Loop").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addpurisma")
def addpurisma():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Purisma Creek Trail").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addridge")
def addridge():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Rission Ridge Trail").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addteresa")
def addteresa():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Santa Teresa Mine Loop").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addsaratoga")
def addsaratoga():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Saratoga Gap Trail").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


@app.route("/addsequoia")
def addsequoia():
    if "username" not in session:
        flash("Sign up to add", "info")
        return redirect(url_for("signup"))
    else:
        hike = db_session.query(Hike).where(
            Hike.name == "Sequoia Bayview Trail").first()
        userhike = Userhike(user_id=session["username"], hike_id=hike.id)
        db_session.add(userhike)
        db_session.commit()
        return render_template("youradventuresofar.html", user=session["username"])


init_db()

if __name__ == "__main__":
    app.run(debug=True)
