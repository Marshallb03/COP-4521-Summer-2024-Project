from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = usname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")
    
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

