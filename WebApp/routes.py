from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from WebApp import db
from WebApp.models import User, College


routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/index')
def index():
    return render_template('index.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        if uname == "Admin" and passw == "password":
            return redirect(url_for("routes.dashboard"))
        else:
            flash("Invalid username or password.")
    
    return render_template("login.html")

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@routes.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    if request.method == "POST":
        uname = request.form['uname']
        passw = request.form['passw']

        register = User(Username=uname, Password=passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("routes.login"))
    return render_template("register.html")

@routes.route('/delete/<int:university_id>', methods=['POST'])
def delete(university_id):
    university_to_delete = College.query.get_or_404(university_id)
    db.session.delete(university_to_delete)
    db.session.commit()
    return redirect(url_for('routes.dashboard'))

@routes.route('/dashboard')
def dashboard():
    universities = College.query.all()
    return render_template('dashboard.html', universities=universities)


@routes.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        university_name = request.form['university_name']
        acceptance_rate = request.form['acceptance_rate']
        average_sat = request.form['average_sat']
        qs_world_rankings = request.form['qs_world_rankings']
        us_news_ranking_2023 = request.form['us_news_ranking_2023']
        qs_world_ranking_2022 = request.form['qs_world_ranking_2022']
        undergraduate_population = request.form['undergraduate_population']
        academic_grade = request.form['academic_grade']
        athletic_grade = request.form['athletic_grade']
        campus_grade = request.form['campus_grade']
        campus_food_grade = request.form['campus_food_grade']
        diversity_grade = request.form['diversity_grade']
        dorms_grade = request.form['dorms_grade']
        location_grade = request.form['location_grade']
        overall_grade = request.form['overall_grade']
        party_scene_grade = request.form['party_scene_grade']
        professors_grade = request.form['professors_grade']
        safety_grade = request.form['safety_grade']
        student_life_grade = request.form['student_life_grade']
        value_grade = request.form['value_grade']
        in_state_tuition = request.form['in_state_tuition']
        out_of_state_tuition = request.form['out_of_state_tuition']

        new_college = College(
            UniversityName=university_name,
            AcceptanceRate=acceptance_rate,
            AverageSAT=average_sat,
            QSWorldRankings=qs_world_rankings,
            USNewsRanking2023=us_news_ranking_2023,
            QSWorldRanking2022=qs_world_ranking_2022,
            UndergraduatePopulation=undergraduate_population,
            AcademicGrade=academic_grade,
            AthleticGrade=athletic_grade,
            CampusGrade=campus_grade,
            CampusFoodGrade=campus_food_grade,
            DiversityGrade=diversity_grade,
            DormsGrade=dorms_grade,
            LocationGrade=location_grade,
            OverallGrade=overall_grade,
            PartySceneGrade=party_scene_grade,
            ProfessorsGrade=professors_grade,
            SafetyGrade=safety_grade,
            StudentLifeGrade=student_life_grade,
            ValueGrade=value_grade,
            InStateTuition=in_state_tuition,
            OutOfStateTuition=out_of_state_tuition
        )

        db.session.add(new_college)
        db.session.commit()

        return redirect(url_for('routes.search'))

    return render_template('create.html')



@routes.route('/search', methods=['GET', 'POST'])
def search():
    colleges = College.query.all()
    selected_college = None
    
    if request.method == 'POST':
        college_name = request.form['university']
        selected_college = College.query.filter_by(UniversityName=college_name).first()
    
    return render_template('search.html', colleges=colleges, selected_college=selected_college)

@routes.route('/update/<int:university_id>', methods=['GET'])
def edit_university(university_id):
    university = College.query.get_or_404(university_id)
    return render_template('update.html', university=university)

@routes.route('/update/<int:university_id>', methods=['POST'])
def update_university(university_id):
    university = College.query.get_or_404(university_id)

    university.UniversityName = request.form['university_name']
    university.AcceptanceRate = request.form['acceptance_rate']
    university.AverageSAT = request.form['average_sat']
    university.QSWorldRankings = request.form['qs_world_rankings']
    university.USNewsRanking2023 = request.form['us_news_ranking_2023']
    university.QSWorldRanking2022 = request.form['qs_world_ranking_2022']
    university.UndergraduatePopulation = request.form['undergraduate_population']
    university.AcademicGrade = request.form['academic_grade']
    university.AthleticGrade = request.form['athletic_grade']
    university.CampusGrade = request.form['campus_grade']
    university.CampusFoodGrade = request.form['campus_food_grade']
    university.DiversityGrade = request.form['diversity_grade']
    university.DormsGrade = request.form['dorms_grade']
    university.LocationGrade = request.form['location_grade']
    university.OverallGrade = request.form['overall_grade']
    university.PartySceneGrade = request.form['party_scene_grade']
    university.ProfessorsGrade = request.form['professors_grade']
    university.SafetyGrade = request.form['safety_grade']
    university.StudentLifeGrade = request.form['student_life_grade']
    university.ValueGrade = request.form['value_grade']
    university.InStateTuition = request.form['in_state_tuition']
    university.OutOfStateTuition = request.form['out_of_state_tuition']

    db.session.commit()
    return redirect(url_for('routes.dashboard'))




