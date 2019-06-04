"""Utility file to seed data from data table to database"""

from sqlalchemy import func
from model import Clinic, Rate, Service
from fractions import Fraction


from model import connect_to_db, db
from server import app
import csv


def convert_to_float(str):
    try: 
        if "/" in str:
            return float(Fraction("".join(str.split(" "))))*100
        else:
            return float(str)

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

        is_sart, is_surrogates, is_single, is_eggcryo, is_embryocryo, is_donor_emb, is_donor_egg = row[-3:-10:-1]


        clinic = Clinic(clinic_name=clinic_name, city=city, state=state, director=director)

        rate = Rate(fresh_mul_1=fresh_mul_1, fresh_mul_2=fresh_mul_2, fresh_mul_3=fresh_mul_3, fresh_mul_4=fresh_mul_4, fresh_mul_5=fresh_mul_5,
                    fresh_sin_1=fresh_sin_1, fresh_sin_2=fresh_sin_2, fresh_sin_3=fresh_sin_3, fresh_sin_4=fresh_sin_4, fresh_sin_5=fresh_sin_5, 
                    fro_mul_1=fro_mul_1, fro_mul_2=fro_mul_2, fro_mul_3=fro_mul_3, fro_mul_4=fro_mul_4, fro_mul_5=fro_mul_5,
                    fro_sin_1=fro_sin_1, fro_sin_2=fro_sin_2, fro_sin_3=fro_sin_3, fro_sin_4=fro_sin_4, fro_sin_5=fro_sin_5)

        service = Service(is_sart=is_sart, is_surrogates=is_surrogates, is_single=is_single, is_eggcryo=is_eggcryo,
                        is_embryocryo=is_embryocryo, is_donor_emb=is_donor_emb, is_donor_egg=is_donor_egg)

        
        rate.clinic = clinic

        db.session.add(clinic)

        service.clinic = clinic

        # add to the session or it won't ever be stored
        
        db.session.add(service)



    # Once done, commit
    db.session.commit()


# def load_services(file_rows):
#     """Load lists of services each clinic provides into database"""

#     print("Services")

#     # read each file row and seeding data
#     for row in file_rows:

#         is_sart = row[-3:]

#         is_sart, is_surrogates, is_single, is_eggcryo, is_embryocryo, is_donor_emb, is_donor_egg = row[-3: -10: -1]
#         print(is_sart)

    
#         service = Service(is_sart=is_sart, is_surrogates=is_surrogates, is_single=is_single, is_eggcryo=is_eggcryo,
#                                 is_embryocryo=is_embryocryo, is_donor_emb=is_donor_emb, is_donor_egg=is_donor_egg)
#         # print(service_list)

#         clinic = Clinic(clinic_name=clinic_name, city=city, state=state, director=director)


#         service_list.clinic = clinic

#         db.session.add(service_list)

#     db.session.commit()






    
if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    filename = "static/2016 data-1.csv"

    rows = load_file(filename)
    load_clinics(rows)
    # load_services(rows)
    









