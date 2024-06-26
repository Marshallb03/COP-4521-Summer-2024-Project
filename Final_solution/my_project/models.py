from my_project import db


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UniversityName = db.Column(db.String(128), nullable=False)
    AcceptanceRate = db.Column(db.Float, nullable=False)
    AverageSAT = db.Column(db.Integer, nullable=False)
    QSWorldRankings = db.Column(db.Integer, nullable=False)
    USNewsRanking2023 = db.Column(db.Integer, nullable=False)
    QSWorldRanking2022 = db.Column(db.Integer, nullable=False)
    UndergraduatePopulation = db.Column(db.Integer, nullable=False)
    AcademicGrade = db.Column(db.Integer, nullable=False)
    AthleticGrade = db.Column(db.Integer, nullable=False)
    CampusGrade = db.Column(db.Integer, nullable=False)
    CampusFoodGrade = db.Column(db.Integer, nullable=False)
    DiversityGrade = db.Column(db.Integer, nullable=False)
    DormsGrade = db.Column(db.Integer, nullable=False)
    LocationGrade = db.Column(db.Integer, nullable=False)
    OverallGrade = db.Column(db.Integer, nullable=False)
    PartySceneGrade = db.Column(db.Integer, nullable=False)
    ProfessorsGrade = db.Column(db.Integer, nullable=False)
    SafetyGrade = db.Column(db.Integer, nullable=False)
    StudentLifeGrade = db.Column(db.Integer, nullable=False)
    ValueGrade = db.Column(db.Integer, nullable=False)
    InStateTuition = db.Column(db.Integer, nullable=False)
    OutOfStateTuition = db.Column(db.Integer, nullable=False)

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    pass_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '' % self.username
