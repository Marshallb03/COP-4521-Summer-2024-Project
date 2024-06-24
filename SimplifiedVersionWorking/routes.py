from flask import render_template, request
from my_project import app, db
from my_project.models import University

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        criteria = request.form['criteria']
        min_value = request.form['min_value']
        max_value = request.form['max_value']
        
        universities = University.query.filter(getattr(University, criteria).between(min_value, max_value)).all()
        return render_template('search_results.html', universities=universities)
    return render_template('search.html')
