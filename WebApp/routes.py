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
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = User.query.filter_by(Username=uname, Password=passw).first()
        if login:
            login_user(login)
            return redirect(url_for("routes.index"))
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

@routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@routes.route('/college/add', methods=['GET', 'POST'])
@login_required
def add_college():
    if current_user.role != 'admin':
        return redirect(url_for('routes.dashboard'))
    form = CollegeForm()
    if form.validate_on_submit():
        college = College(
            UniversityName=form.university_name.data,
            AcceptanceRate=form.acceptance_rate.data,
            AverageSAT=form.average_sat.data,
            QSWorldRankings=form.qs_world_rankings.data,
            USNewsRanking2023=form.us_news_ranking_2023.data,
            QSWorldRanking2022=form.qs_world_rankings_2022.data,
            UndergraduatePopulation=form.undergraduate_population.data,
            AcademicGrade=form.academic_grade.data,
            AthleticGrade=form.athletic_grade.data,
            CampusGrade=form.campus_grade.data,
            CampusFoodGrade=form.campus_food_grade.data,
            DiversityGrade=form.diversity_grade.data,
            DormsGrade=form.dorms_grade.data,
            LocationGrade=form.location_grade.data,
            OverallGrade=form.overall_grade.data,
            PartySceneGrade=form.party_scene_grade.data,
            ProfessorsGrade=form.professors_grade.data,
            SafetyGrade=form.safety_grade.data,
            StudentLifeGrade=form.student_life_grade.data,
            ValueGrade=form.value_grade.data,
            InStateTuition=form.in_state_tuition.data,
            OutOfStateTuition=form.out_of_state_tuition.data
        )
        db.session.add(college)
        db.session.commit()
        flash('College added successfully.', 'success')
        return redirect(url_for('routes.dashboard'))
    return render_template('add_college.html', form=form)



@routes.route('/college/delete/<int:college_id>', methods=['POST'])
@login_required
def delete_college(college_id):
    if current_user.role != 'admin':
        return redirect(url_for('routes.dashboard'))
    college = College.query.get_or_404(college_id)
    db.session.delete(college)
    db.session.commit()
    flash('College deleted successfully.', 'success')
    return redirect(url_for('routes.dashboard'))


@routes.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        colleges = College.query.filter(College.UniversityName.ilike('%' + form.university_name.data + '%'))
        return render_template('search_results.html', colleges=colleges)
    return render_template('search.html', form=form)
