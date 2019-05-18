from flask_sqlalchemy import SQLAlchemy


# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class Clinic(db.Model):
    """Provide clinics info"""

    __tablename__ = "clinics"

    clinic_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    clinic_name = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(200))
    director = db.Column(db.String(200))


    # director_id = db.Column(db.Integer, db.ForeignKey('directors.director_id'))
    # city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))
    
    # rate_id = db.Column(db.Integer, db.ForeignKey('rates.rate_id'))

    # Define relationship to city
    # city = db.relationship("City",
    #                        backref=db.backref("clinics"))

    # Define relationship to director
    # director = db.relationship("Director", backref=db.backref("clinics"))

    # Define relationship to rating
    # rate = db.relationship("Rate", backref=db.backref("clinics"))


    def __repr__(self):
        """Provide complete info about each clinic object"""

        # return f"<Clinic clinic_id={self.clinic_id} director_id={self.director_id} city_id={self.city_id} clinic_name={self.clinic_name}>"
        # return f"<Clinic clinic_id={self.clinic_id} director={self.director} city={self.city} state={self.state} clinic_name={self.clinic_name} rate_id={self.rate_id}>"

        return f"<Clinic clinic_id={self.clinic_id} clinic_name={self.clinic_name} city={self.city} state={self.state} director={self.director}>"


class Rate(db.Model):
    """Provide ratings for each clinic"""

    __tablename__ = "rates"

    rate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    is_single_bool = db.Column(db.Boolean)
    is_fresh_emb = db.Column(db.Boolean)
    rate_group_1 = db.Column(db.Float, nullable=True)
    rate_group_2 = db.Column(db.Float, nullable=True)
    rate_group_3 = db.Column(db.Float, nullable=True)
    rate_group_4 = db.Column(db.Float, nullable=True)
    rate_group_5 = db.Column(db.Float, nullable=True)

    clinic = db.relationship("Clinic", 
                            secondary="clinic-rates", 
                            backref="rates")

    # clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.clinic_id'))
    # age_id = db.Column(db.Integer, db.ForeignKey('age-ranges.age_id'))


    def __repr__(self):

        return f"<Rates rate_id={self.rate_id} is_single_bool={self.is_single_bool} is_fresh_emb={self.is_fresh_emb} rate_group_1={self.rate_group_1} rate_group_2={self.rate_group_2} rate_group_3={self.rate_group_3} rate_group_4={self.rate_group_4} rate_group_5={self.rate_group_5}>"


# class ClinicRate(db.Model):
#     """Rate of a specific clinic"""

#     __tablename__ = "clinic-rates"

#     clinic_rate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.clinic_id'))
#     rate_id = db.Column(db.Integer, db.ForeignKey('rates.rate_id'))

#     def __repr__(self):
#         """"""

#         return f"<Clinic Rates clinic_rate_id={self.clinic_rate_id} clinic_id={self.clinic_id} rate_id={self.rate_id}>"

  
# # # class ClinicRate(db.Model):
# # #     """Association Table"""
# # #     clinic_rate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# # #     clinic_id = db.Column(db.Integer, db.ForeignKey(''))


# # # class Director(db.Model):
# # #     """Director name for each clinic"""

# # #     __tablename__ = "directors"

# #     director_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# #     director_name = db.Column(db.String(30))

# #     def __repr__(self):
# #         """Provide info about each clinic's director"""

# #         return f"<Director director_id={self.director_id} director_name={self.director_name}>"



# # class City(db.Model):
# #     """Provide name of city associated with each clinic"""

# #     __tablename__ = "cities"

# #     city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# #     city_name = db.Column(db.String(30))
# #     state_id = db.Column(db.Integer, db.ForeignKey('states.state_id'))

# #     # Define relationship to state
# #     state = db.relationship("City", backref=db.backref("cities"))

# #     def __repr__(self):
# #         """provide city info for each city object"""

# #         return f"<City city_id={self.city_id} city_name={self.city_name}>"


# # class State(db.Model):
# #     """Provide state of each clinic"""

# #     __tablename__ = "states"

# #     state_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# #     state_name = db.Column(db.String(30))

# #     def __repr__(self):
# #         """Provide state info for each state object"""

# #         return f"<State state_id={self.state_id} state_name={self.state_name}>"

# class AgeRange(db.Model):
#     """Provide age ranges"""

#     __tablename__ = "age-ranges"

#     age_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     age_range = db.Column(db.String(30))

#     def __repr__(self):
#         """Provide age ranges for each age object"""

#         return f"<Age Ranges age_id={age_id} age_range={age_range}>" 


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///rates'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")








    

    