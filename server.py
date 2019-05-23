from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import Clinic, Rate

from model import connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined




@app.route('/', methods=["GET"])
def index():
    """Homepage."""

    return render_template('map.html')




@app.route('/get-state-city', methods=["POST"])
def get_state_city():
    """Return a list of clinics corresponding to a particular state and city"""


    user_state = request.form.get("state")

    user_city = request.form.get('city').upper()

    state_clinics = Clinic.query.filter_by(state=user_state).all()

    cities = []

    for clinic in state_clinics:
        city = clinic.city
        cities.append(city)

    if user_city in cities:
        user_clinics = Clinic.query.filter_by(city=user_city).all()
    else:
        return redirect('/')

    return render_template('show_list.html', user_clinics=user_clinics, user_state=user_state)





@app.route('/show_rates/<clinic_name>')
def show_rates(clinic_name):
    """Provide success rates of each clinic"""

    desired_clinics = Clinic.query.filter_by(clinic_name=clinic_name).first()

    clinic_id = desired_clinics.clinic_id


    rates = Rate.query.filter_by(clinic_id=clinic_id)

    # clinic_id = Clinic.query.filter_by(clinic_name=clinic_name)


    # rates = Rate.query.filter(Rate.clinic_id==clinic_id).all()

    return render_template('/show_rates.html', rates=rates, clinic_name=clinic_name)



    
                                        

        



    





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")




