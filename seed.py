"""Utility file to seed data from data table to database"""

from sqlalchemy import func
from model import Clinic, Rate
from fractions import Fraction


from model import connect_to_db, db
from server import app
import csv


def convert_to_float(str):
    try: 
        # return float(Fraction("".join(str.split(" "))))*100
        return float((Fraction(str.split(" ")))*100)

    except ValueError:
        return None


def load_file(filename):
    """Open and read a given filename"""

    rows = []

    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, quotechar='"', delimiter=",")
        
        for row in spamreader:
            rows.append(row)
    return rows


def load_clinics(file_rows):
    """Load clinics into database"""

    print("Clinics")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    # Clinic.query.delete()

    # Read file_rows and insert data
    for row in file_rows[1:]:
         # unpack part of each row
        clinic_id, clinic_name, city, state, director = row[:5]
        fresh_mul_1, fresh_mul_2, fresh_mul_3, fresh_mul_4, fresh_mul_5= map(convert_to_float, row[5:10])
        fresh_sin_1, fresh_sin_2, fresh_sin_3, fresh_sin_4, fresh_sin_5 = map(convert_to_float, row[10:15]) 
        fro_mul_1, fro_mul_2, fro_mul_3, fro_mul_4, fro_mul_5 = map(convert_to_float, row[15:20])
        fro_sin_1, fro_sin_2, fro_sin_3, fro_sin_4, fro_sin_5 = map(convert_to_float, row[20:25])


        clinic = Clinic(clinic_name=clinic_name, city=city, state=state, director=director)

        rate = Rate(fresh_mul_1=fresh_mul_1, fresh_mul_2=fresh_mul_2, fresh_mul_3=fresh_mul_3, fresh_mul_4=fresh_mul_4, fresh_mul_5=fresh_mul_5,
                    fresh_sin_1=fresh_sin_1, fresh_sin_2=fresh_sin_2, fresh_sin_3=fresh_sin_3, fresh_sin_4=fresh_sin_4, fresh_sin_5=fresh_sin_5, 
                    fro_mul_1=fro_mul_1, fro_mul_2=fro_mul_2, fro_mul_3=fro_mul_3, fro_mul_4=fro_mul_4, fro_mul_5=fro_mul_5,
                    fro_sin_1=fro_sin_1, fro_sin_2=fro_sin_2, fro_sin_3=fro_sin_3, fro_sin_4=fro_sin_4, fro_sin_5=fro_sin_5)
        
        rate.clinic = clinic
        # add to the session or it won't ever be stored
        
        db.session.add(clinic)

    # Once done, commit
    db.session.commit()










    
if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    filename = "static/2016 data-1.csv"

    rows = load_file(filename)
    load_clinics(rows)
    









