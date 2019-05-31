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

    rate_data = db.relationship("Rate", backref="clinic",
                                        uselist=False)

    service_list = db.relationship("Service", backref="clinic",
                                        uselist=False)

    def __repr__(self):
        """Provide complete info about each clinic object"""

        return f"<Clinic clinic_id={self.clinic_id} clinic_name={self.clinic_name} city={self.city} state={self.state} director={self.director}>"


class Rate(db.Model):
    """Provide ratings for each clinic"""

    __tablename__ = "rates"

    rate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.clinic_id'))
    
    fresh_mul_1 = db.Column(db.Float, nullable=True)
    fresh_mul_2 = db.Column(db.Float, nullable=True)
    fresh_mul_3 = db.Column(db.Float, nullable=True)
    fresh_mul_4 = db.Column(db.Float, nullable=True)
    fresh_mul_5 = db.Column(db.Float, nullable=True)

    fresh_sin_1 = db.Column(db.Float, nullable=True)
    fresh_sin_2 = db.Column(db.Float, nullable=True)
    fresh_sin_3 = db.Column(db.Float, nullable=True)
    fresh_sin_4 = db.Column(db.Float, nullable=True)
    fresh_sin_5 = db.Column(db.Float, nullable=True)

    fro_mul_1 = db.Column(db.Float, nullable=True)
    fro_mul_2 = db.Column(db.Float, nullable=True)
    fro_mul_3 = db.Column(db.Float, nullable=True)
    fro_mul_4 = db.Column(db.Float, nullable=True)
    fro_mul_5 = db.Column(db.Float, nullable=True)

    fro_sin_1 = db.Column(db.Float, nullable=True)
    fro_sin_2 = db.Column(db.Float, nullable=True)
    fro_sin_3 = db.Column(db.Float, nullable=True)
    fro_sin_4 = db.Column(db.Float, nullable=True)
    fro_sin_5 = db.Column(db.Float, nullable=True)  
    


    def __repr__(self):

        return f"""<Rates rate_id={self.rate_id}
                        fresh_mul_1={self.fresh_mul_1} fresh_mul_2={self.fresh_mul_2} fresh_mul_3={self.fresh_mul_3} fresh_mul_4={self.fresh_mul_4} fresh_mul_5={self.fresh_mul_5} 
                        fresh_sin_1={self.fresh_sin_1} fresh_sin_2={self.fresh_sin_2} fresh_sin_3={self.fresh_sin_3} fresh_sin_4={self.fresh_sin_4} fresh_sin_5={self.fresh_sin_5}
                        fro_mul_1={self.fro_mul_1} fro_mul_2={self.fro_mul_2} fro_mul_3={self.fro_mul_3} fro_mul_4={self.fro_mul_4} fro_mul_5={self.fro_mul_5}
                        fro_sin_1={self.fro_sin_1} fro_sin_2={self.fro_sin_2} fro_sin_3={self.fro_sin_3} fro_sin_4={self.fro_sin_4} fro_sin_5={self.fro_sin_5}>"""



class Service(db.Model):
    """Provide a list of services each clinic provides"""

    __tablename__ = "services"

    service_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.clinic_id'))
    is_sart = db.Column(db.String(200))
    is_surrogates = db.Column(db.String(200))
    is_single = db.Column(db.String(200))
    is_eggcryo = db.Column(db.String(200))
    is_embryocryo = db.Column(db.String(200))
    is_donor_emb = db.Column(db.String(200))
    is_donor_egg = db.Column(db.String(200))

    def __repr__(self):

        return f"""<Services is_sart={self.is_sart} is_surrogates={self.is_surrogates} is_single={self.is_single} is_eggcryo={self.is_eggcryo}
                            is_embryocryo={self.is_embryocryo} is_donor_emb={self.is_donor_emb} is_donor_egg={self.is_donor_egg}>"""




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








    

    