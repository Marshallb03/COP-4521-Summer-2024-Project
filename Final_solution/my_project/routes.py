from flask import render_template, request, redirect, url_for, flash , session
from my_project import app, db
from my_project.models import University
from my_project.models import User
from werkzeug.security import generate_password_hash , check_password_hash
import sqlalchemy


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")
    

@app.route("/dashboard/")
def dashboard():
    universities = University.query.all()
    return render_template("dashboard.html", universities=universities)

@app.route("/create/", methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        UniversityName = request.form['UniversityName']
        AcceptanceRate = float(request.form['AcceptanceRate'])
        AverageSAT = int(request.form['AverageSAT'])
        QSWorldRankings = int(request.form['QSWorldRankings'])
        USNewsRanking2023 = int(request.form['USNewsRanking2023'])
        QSWorldRanking2022 = int(request.form['QSWorldRanking2022'])
        UndergraduatePopulation = int(request.form['UndergraduatePopulation'])
        AcademicGrade = int(request.form['AcademicGrade'])
        AthleticGrade = int(request.form['AthleticGrade'])
        CampusGrade = int(request.form['CampusGrade'])
        CampusFoodGrade = int(request.form['CampusFoodGrade'])
        DiversityGrade = int(request.form['DiversityGrade'])
        DormsGrade = int(request.form['DormsGrade'])
        LocationGrade = int(request.form['LocationGrade'])
        OverallGrade = int(request.form['OverallGrade'])
        PartySceneGrade = int(request.form['PartySceneGrade'])
        ProfessorsGrade = int(request.form['ProfessorsGrade'])
        SafetyGrade = int(request.form['SafetyGrade'])
        StudentLifeGrade = int(request.form['StudentLifeGrade'])
        ValueGrade = int(request.form['ValueGrade'])
        InStateTuition = int(request.form['InStateTuition'])
        OutOfStateTuition = int(request.form['OutOfStateTuition'])

        new_university = University(
            UniversityName=UniversityName,
            AcceptanceRate=AcceptanceRate,
            AverageSAT=AverageSAT,
            QSWorldRankings=QSWorldRankings,
            USNewsRanking2023=USNewsRanking2023,
            QSWorldRanking2022=QSWorldRanking2022,
            UndergraduatePopulation=UndergraduatePopulation,
            AcademicGrade=AcademicGrade,
            AthleticGrade=AthleticGrade,
            CampusGrade=CampusGrade,
            CampusFoodGrade=CampusFoodGrade,
            DiversityGrade=DiversityGrade,
            DormsGrade=DormsGrade,
            LocationGrade=LocationGrade,
            OverallGrade=OverallGrade,
            PartySceneGrade=PartySceneGrade,
            ProfessorsGrade=ProfessorsGrade,
            SafetyGrade=SafetyGrade,
            StudentLifeGrade=StudentLifeGrade,
            ValueGrade=ValueGrade,
            InStateTuition=InStateTuition,
            OutOfStateTuition=OutOfStateTuition
        )

        # Add the new university record to the database
        db.session.add(new_university)
        db.session.commit()

        return render_template('create_result.html')

    return render_template("create.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
   
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Username or Password cannot be empty.")
            return redirect(url_for('login'))
        else:
            username = username.strip()
            password = password.strip()

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.pass_hash, password):
            session[username] = True
            return  render_template('dashboard.html')
  
        else:
            flash("Invalid username or password.")


    
    return render_template("login.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        criteria = request.form['criteria']
        min_value = request.form['min_value']
        max_value = request.form['max_value']
        
        universities = University.query.filter(getattr(University, criteria).between(min_value, max_value)).all()
        return render_template('search_results.html', universities=universities)
    return render_template('search.html')

@app.route("/signup/", methods=["GET", "POST"])
def signup():
   
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Username or Password cannot be empty")
            return redirect(url_for('signup'))
        else:
            username = username.strip()
            password = password.strip()

        hashed_pwd = generate_password_hash(password)

        new_user = User(username=username, pass_hash=hashed_pwd)
        db.session.add(new_user)

        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            flash("Username {u} is not available.".format(u=username))
            return redirect(url_for('signup'))

        flash("User account has been created.")
        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        university_name = request.form.get('UniversityName')

        if university_name:
            university = University.query.filter_by(UniversityName=university_name).first()

            if university:
                db.session.delete(university)
                db.session.commit()
                flash(f'University {university_name} has been deleted successfully', 'success')
            else:
                flash(f'University with name {university_name} not found', 'error')
        else:
            flash('University name is required for deletion', 'error')

        return render_template('delete_result.html')

    return render_template('delete.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

  