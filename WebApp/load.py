import pandas as pd
from flask import Flask
from . import create_app, db  # Adjust the import to your Flask factory if necessary
from .models import College  # Adjust this import based on your actual module structure

app = create_app()  # Create an instance of your Flask app

def load_data():
    # Run within application context
    with app.app_context():
        data = pd.read_csv('UniversityDB.csv')

        for index, row in data.iterrows():
            new_college = College(
                UniversityID=row['UNIVERSITYID'],
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
            db.session.add(new_college)
        db.session.commit()

if __name__ == '__main__':
    load_data()
