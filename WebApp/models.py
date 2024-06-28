from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.UserID')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)

class User(UserMixin, db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255), unique=True)
    Password = db.Column(db.String(255))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class College(db.Model):
    __tablename__ = 'universities'
    
    UniversityID = db.Column(db.Integer, primary_key=True, autoincrement=True, name='UNIVERSITYID')
    UniversityName = db.Column(db.String(255), name='University Name')
    AcceptanceRate = db.Column(db.Integer, name='Acceptance Rate')
    AverageSAT = db.Column(db.Integer, name='Average SAT')
    AcademicGrade = db.Column(db.String(5), name='Niche Academic Grade')
    AthleticGrade = db.Column(db.String(5), name='Niche Athletic Grade')
    CampusGrade = db.Column(db.String(5), name='Niche Campus Grade')
    CampusFoodGrade = db.Column(db.String(5), name='Niche Campus Food Grade')
    DiversityGrade = db.Column(db.String(5), name='Niche Diversity Grade')
    DormsGrade = db.Column(db.String(5), name='Niche Dorms Grade')
    LocationGrade = db.Column(db.String(5), name='Niche Location Grade')
    OverallGrade = db.Column(db.String(5), name='Niche Overall Grade')
    PartySceneGrade = db.Column(db.String(5), name='Niche Party Scene Grade')
    ProfessorsGrade = db.Column(db.String(5), name='Niche Professors Grade')
    SafetyGrade = db.Column(db.String(5), name='Niche Safety Grade')
    StudentLifeGrade = db.Column(db.String(5), name='Niche Student Life Grade')
    ValueGrade = db.Column(db.String(5), name='Niche Value Grade')
    QSWorldRankings = db.Column(db.Integer, name='QS World Rankings')
    UndergraduatePopulation = db.Column(db.Integer, name='Undergraduate Population')
    USNewsRanking2023 = db.Column(db.Integer, name='2023 US News Ranking')
    QSWorldRanking2022 = db.Column(db.Integer, name='2022 QS World Ranking')
    InStateTuition = db.Column(db.Float, name='In-State Tuition')
    OutOfStateTuition = db.Column(db.Float, name='Out-of-State Tuition')



