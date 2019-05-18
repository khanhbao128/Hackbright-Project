"""Utility file to seed data from data table to database"""

from sqlalchemy import func
from model import Clinic
# from model import City
# from model import State
# from model import AgeRange

from model import connect_to_db, db
from server import app
import csv



def load_file(filename):
    """Open and read a given filename"""

    rows = []

    with open('statics/2016 data.csv') as csvfile:
        spamreader = csv.reader(csvfile, quotechar='"', delimiter=",")
        for row in spamreader:
            rows.append(row)
        return rows



def load_clinics(file_rows):
    """Load clinics into database"""

    print("Clinics")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Clinic.query.delete()

    # Read file_rows and insert data
    for row in file_rows[1:]:
         # unpack part of each row
        clinic_id, clinic_name, city, state, director = row[:5]

        # seeding data to database
        # clinic = Clinic(clinic_id=clinic_id,
                        # clinic_name=clinic_name,
                        # city=city,
                        # state=state,
                        # director=director)

        clinic = Clinic(clinic_id=clinic_id, clinic_name=clinic_name, city=city, state=state, director=director)
        
        # print(clinic_id, clinic_name, city, state, director)
        # add to the session or it won't ever be stored
        db.session.add(clinic)

    # Once done, commit
    db.session.commit()


def load_rates(file_rows):
    """Load rates from file into database"""

    print("Rates")

    Rate.query.delete()

    for row in file_rows[1:]:
        if is_fresh_emb_bool == True:
            if is_single_bool == False:
                rate_group_1, rate_group_2, rate_group_3, rate_group_4, rate_group_5 = row[5:11]
            else:
                rate_group_1, rate_group_2, rate_group_3, rate_group_4, rate_group_5 = row[11:16]

        else:
            if is_single_bool == False:
                rate_group_1, rate_group_2, rate_group_3, rate_group_4, rate_group_5 = row[16:21]
            else:
                rate_group_1, rate_group_2, rate_group_3, rate_group_4, rate_group_5 = row[21:26]

        rate = Rate(rate_group_1=rate_group_1, rate_group_2=rate_group_2, rate_group_3=rate_group_3, rate_group_4=rate_group_4, rate_group_5=rate_group_5)

        # add to the session
        db.session.add(rate)

    db.session.commit()










    
if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    filename = "statics/2016 data.csv"

    rows = load_file(filename)
    load_clinics(rows)
    load_rates(rows)   

    # directors = load_director(rows)








