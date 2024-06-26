import csv
from my_project import db, app  # Use absolute imports
from my_project.models import University

def populate_db():
    with app.app_context():
        db.create_all()
        with open('UniversityDB.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                university = University(
                    UniversityName=row['UniversityName'],
                    AcceptanceRate=row['AcceptanceRate'],
                    AverageSAT=row['AverageSAT'],
                    QSWorldRankings=row['QSWorldRankings'],
                    USNewsRanking2023=row['USNewsRanking2023'],
                    QSWorldRanking2022=row['QSWorldRanking2022'],
                    UndergraduatePopulation=row['UndergraduatePopulation'],
                    AcademicGrade=row['AcademicGrade'],
                    AthleticGrade=row['AthleticGrade'],
                    CampusGrade=row['CampusGrade'],
                    CampusFoodGrade=row['CampusFoodGrade'],
                    DiversityGrade=row['DiversityGrade'],
                    DormsGrade=row['DormsGrade'],
                    LocationGrade=row['LocationGrade'],
                    OverallGrade=row['OverallGrade'],
                    PartySceneGrade=row['PartySceneGrade'],
                    ProfessorsGrade=row['ProfessorsGrade'],
                    SafetyGrade=row['SafetyGrade'],
                    StudentLifeGrade=row['StudentLifeGrade'],
                    ValueGrade=row['ValueGrade'],
                    InStateTuition=row['InStateTuition'],
                    OutOfStateTuition=row['OutOfStateTuition']
                )
                db.session.add(university)
            db.session.commit()

if __name__ == '__main__':
    populate_db()
