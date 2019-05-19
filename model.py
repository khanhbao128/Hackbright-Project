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




    def __repr__(self):
        """Provide complete info about each clinic object"""

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


    def __repr__(self):

        return f"<Rates rate_id={self.rate_id} is_single_bool={self.is_single_bool} is_fresh_emb={self.is_fresh_emb} rate_group_1={self.rate_group_1} rate_group_2={self.rate_group_2} rate_group_3={self.rate_group_3} rate_group_4={self.rate_group_4} rate_group_5={self.rate_group_5}>"


class ClinicRate(db.Model):
    """Rate of a specific clinic"""

    __tablename__ = "clinic-rates"

    clinic_rate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.clinic_id'))
    rate_id = db.Column(db.Integer, db.ForeignKey('rates.rate_id'))

    def __repr__(self):
        """"""

        return f"<Clinic Rates clinic_rate_id={self.clinic_rate_id} clinic_id={self.clinic_id} rate_id={self.rate_id}>"


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








    

    