from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import app, db, login_manager
from .models import User, College
from .forms import LoginForm, RegistrationForm, SearchForm, CollegeForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(Username=form.username.data).first()
        if user and user.Password == form.password.data:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(Username=form.username.data, Email=form.email.data, Password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/college/add', methods=['GET', 'POST'])
@login_required
def add_college():
    if current_user.role != 'admin':
        return redirect(url_for('dashboard'))
    form = CollegeForm()
    if form.validate_on_submit():
        college = College(UniversityName=form.university_name.data, AcceptanceRate=form.acceptance_rate.data, AverageSAT=form.average_sat.data, 
        QSWorldRankings=form.qs_world_rankings.data, USNewsRanking2023=form.us_news_ranking_2023.data, QSWorldRanking2022=form.qs_world_ranking_2022.data, 
        UndergraduatePopulation=form.undergraduate_population.data, AcademicGrade=form.academic_grade.data, AthleticGrade=form.athletic_grade.data, 
        CampusGrade=form.campus_grade.data, CampusFoodGrade=form.campus_food_grade.data, DiversityGrade=form.diversity_grade.data, DormsGrade=form.dorms_grade.data, 
        LocationGrade=form.location_grade.data, OverallGrade=form.overall_grade.data, PartySceneGrade=form.party_scene_grade.data, ProfessorsGrade=form.professors_grade.data, SafetyGrade=form.safety_grade.data, 
        StudentLifeGrade=form.student_life_grade.data, ValueGrade=form.value_grade.data, InStateTuition=form.in_state_tuition.data, OutOfStateTuition=form.out_of_state_tuition.data)
        db.session.add(college)
        db.session.commit()
        flash('College added successfully.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_college.html', form=form)

@app.route('/college/edit/<int:college_id>', methods=['GET', 'POST'])
@login_required
def edit_college(college_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard'))
    college = College.query.get_or_404(college_id)
    form = CollegeForm(obj=college)
    if form.validate_on_submit():
        form.populate_obj(college)
        db.session.commit()
        flash('College updated successfully.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_college.html', form=form)

@app.route('/college/delete/<int:college_id>', methods=['POST'])
@login_required
def delete_college(college_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard'))
    college = College.query.get_or_404(college_id)
    db.session.delete(college)
    db.session.commit()
    flash('College deleted successfully.', 'success')
    return redirect(url_for('dashboard'))

# Example of a search route
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        # Perform search based on form data
        # Example:
        colleges = College.query.filter(College.UniversityName.ilike('%' + form.university_name.data + '%'))
        # Render template with search results
        return render_template('search_results.html', colleges=colleges)
    return render_template('search.html', form=form)

