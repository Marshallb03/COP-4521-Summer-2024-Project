from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    role = db.Column(db.String(80), db.ForeignKey('role.name'))

class College(db.Model):
    UniversityID = db.Column(db.Integer, primary_key=True)
    UniversityName = db.Column(db.String(255))
    AcceptanceRate = db.Column(db.Integer)
    AverageSAT = db.Column(db.Integer)
    QSWorldRankings = db.Column(db.Integer)
    USNewsRanking2023 = db.Column(db.Integer)
    QSWorldRanking2022 = db.Column(db.Integer)
    UndergraduatePopulation = db.Column(db.Integer)
    AcademicGrade = db.Column(db.String(5))
    AthleticGrade = db.Column(db.String(5))
    CampusGrade = db.Column(db.String(5))
    CampusFoodGrade = db.Column(db.String(5))
    DiversityGrade = db.Column(db.String(5))
    DormsGrade = db.Column(db.String(5))
    LocationGrade = db.Column(db.String(5))
    OverallGrade = db.Column(db.String(5))
    PartySceneGrade = db.Column(db.String(5))
    ProfessorsGrade = db.Column(db.String(5))
    SafetyGrade = db.Column(db.String(5))
    StudentLifeGrade = db.Column(db.String(5))
    ValueGrade = db.Column(db.String(5))
    InStateTuition = db.Column(db.Float)
    OutOfStateTuition = db.Column(db.Float)


# class Role(db.Model, RoleMixin):  
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
