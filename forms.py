from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class SearchForm(FlaskForm):
    university_name = StringField('University Name')
    acceptance_rate = IntegerField('Acceptance Rate')
    average_sat = IntegerField('Average SAT')
    qs_world_rankings = IntegerField('QS World Rankings')
    us_news_ranking_2023 = IntegerField('US News Ranking 2023')
    qs_world_ranking_2022 = IntegerField('QS World Ranking 2022')
    undergraduate_population = IntegerField('Undergraduate Population')
    academic_grade = StringField('Academic Grade')
    athletic_grade = StringField('Athletic Grade')
    campus_grade = StringField('Campus Grade')
    campus_food_grade = StringField('Campus Food Grade')
    diversity_grade = StringField('Diversity Grade')
    dorms_grade = StringField('Dorms Grade')
    location_grade = StringField('Location Grade')
    overall_grade = StringField('Overall Grade')
    party_scene_grade = StringField('Party Scene Grade')
    professors_grade = StringField('Professors Grade')
    safety_grade = StringField('Safety Grade')
    student_life_grade = StringField('Student Life Grade')
    value_grade = StringField('Value Grade')
    in_state_tuition = IntegerField('In-State Tuition')
    out_of_state_tuition = IntegerField('Out-of-State Tuition')
    submit = SubmitField('Search')