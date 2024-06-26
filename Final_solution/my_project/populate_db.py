import csv
from my_project import db, app
from my_project.models import University


def populate_db():
    with app.app_context():
        db.create_all()
        with open('UniversityDB.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                university = University(
                    UniversityName=row['University Name'],
                    AcceptanceRate=row['Acceptance Rate'],
                    AverageSAT=row['Average SAT'],
                    QSWorldRankings=row['QS World Rankings'],
                    USNewsRanking2023=row['2023 US News Ranking'],
                    QSWorldRanking2022=row['2022 QS World Ranking'],
                    UndergraduatePopulation=row['Undergraduate Population'],
                    AcademicGrade=row['Niche Academic Grade'],
                    AthleticGrade=row['Niche Athletic Grade'],
                    CampusGrade=row['Niche Campus Grade'],
                    CampusFoodGrade=row['Niche Campus Food Grade'],
                    DiversityGrade=row['Niche Diversity Grade'],
                    DormsGrade=row['Niche Dorms Grade'],
                    LocationGrade=row['Niche Location Grade'],
                    OverallGrade=row['Niche Overall Grade'],
                    PartySceneGrade=row['Niche Party Scene Grade'],
                    ProfessorsGrade=row['Niche Professors Grade'],
                    SafetyGrade=row['Niche Safety Grade'],
                    StudentLifeGrade=row['Niche Student Life Grade'],
                    ValueGrade=row['Niche Value Grade'],
                    InStateTuition=row['In-State Tuition'],
                    OutOfStateTuition=row['Out-of-State Tuition']
                )
                db.session.add(university)
                
            db.session.commit()

if __name__ == '__main__':
    populate_db()
