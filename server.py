from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
import json
import requests
from flask_debugtoolbar import DebugToolbarExtension

from model import Clinic, Rate, Service

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

    return render_template('homepage.html')

def make_API_call(clinic_name, clinic_city):

    input_para = str(clinic_name) + " " + str(clinic_city)

    inputs = input_para.split(" ")

    inputs = "%20".join(inputs)

    inputs = "'" + inputs + "'"
    
    print(inputs)
   
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + inputs + "&inputtype=textquery&fields=formatted_address,geometry&key=AIzaSyDfjxfPTabsjVyZPQT1zp9L1VaB9sjvwxc"

    response = requests.get(url)
    print(response)

    data = response.json()
    print(data)

    if response.ok:

        user_clinic_address = data['candidates'][0]['formatted_address']

        geo_location = data['candidates'][0]['geometry']['location']

        return geo_location


@app.route('/get-state-city', methods=["POST"])
def get_state_city():
    """Return a list of clinics corresponding to a particular state and city"""

    location = request.form.get('location')

    location = location.split(",")

    if location == [] or len(location) < 3:

        flash("Please enter name of a city and pick the city and state from the dropdown menu")

        return redirect("/")

    else:
        
        user_city = location[0].upper()

        user_state = location[1].lstrip()

        state_clinics = Clinic.query.filter_by(state=user_state).all()


        all_cities = []

        for clinic in state_clinics:

            all_cities.append(clinic.city)

        #not all cities have fertility clinics so need to use state input to have a list of all cities that exist in database 
        if user_city in all_cities:

            user_clinics = Clinic.query.filter((Clinic.city==user_city) & (Clinic.state==user_state)).all()
        
            clinic_names = []

            for user_clinic in user_clinics:
                # create the list of clinic names in the state input
                clinic_names.append(user_clinic.clinic_name)


            geo_locations = {}

            longitude = []
            
            latitude = []

            for clinic_name in clinic_names:

                geo_location = make_API_call(clinic_name, user_city)

                longitude.append(geo_location['lng'])

                latitude.append(geo_location['lat'])


            geo_locations['lng'] = longitude

            geo_locations['lat'] = latitude
            

            geo_locations = json.dumps(geo_locations)

           
            return render_template('show_list.html', user_clinics=user_clinics, geo_locations=geo_locations, user_city=user_city, user_state=user_state)
       
        else:

            flash("Sorry there are no clinics found in this city.")

            return redirect('/')


@app.route('/show_services_rates/<clinic_name>')
def show_rates(clinic_name):
    """Provide success rates of each clinic"""

    user_clinic = Clinic.query.filter_by(clinic_name=clinic_name).first()

    user_clinic_id = user_clinic.clinic_id

    user_clinic_name = user_clinic.clinic_name

    user_clinic_city = user_clinic.city

    input_para = str(user_clinic_name) + " " + str(user_clinic_city)

    inputs = input_para.split(" ")

    inputs = "%20".join(inputs)

    inputs = "'" + inputs + "'"
    
    print(inputs)
   
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + inputs + "&inputtype=textquery&fields=formatted_address,geometry&key=AIzaSyDfjxfPTabsjVyZPQT1zp9L1VaB9sjvwxc"

    response = requests.get(url)
    print(response)

    data = response.json()
    print(data)

    if response.ok:

        user_clinic_address = data['candidates'][0]['formatted_address']

        geo_location = data['candidates'][0]['geometry']['location']

        latitude = geo_location['lat']

        longitude = geo_location['lng']

        print(latitude, longitude)


        rates = Rate.query.filter_by(clinic_id=user_clinic_id)
        rate = user_clinic.rate_data
        print(rate)

        # adding all rate attributes to a dictionary, turn that dictionary to json and pass it to 'show_rates.html' so that JS can understand null values (jinja can understand None but JS doesn't. Need to convert None to null by jsonifying)
        rate_dict = {}


        rate_dict['fresh_mul_1'] = rate.fresh_mul_1
        rate_dict['fresh_mul_2'] = rate.fresh_mul_2
        rate_dict['fresh_mul_3'] = rate.fresh_mul_3
        rate_dict['fresh_mul_4'] = rate.fresh_mul_4

        rate_dict['fresh_sin_1'] = rate.fresh_sin_1
        rate_dict['fresh_sin_2'] = rate.fresh_sin_2
        rate_dict['fresh_sin_3'] = rate.fresh_sin_3
        rate_dict['fresh_sin_4'] = rate.fresh_sin_4

        rate_dict['fro_mul_1'] = rate.fro_mul_1
        rate_dict['fro_mul_2'] = rate.fro_mul_2
        rate_dict['fro_mul_3'] = rate.fro_mul_3
        rate_dict['fro_mul_4'] = rate.fro_mul_4

        rate_dict['fro_sin_1'] = rate.fro_sin_1
        rate_dict['fro_sin_2'] = rate.fro_sin_2
        rate_dict['fro_sin_3'] = rate.fro_sin_3
        rate_dict['fro_sin_4'] = rate.fro_sin_4
        # print(rate_dict)

        rate_dict = json.dumps(rate_dict)
        print("HEEERREE", rate_dict)
        print(type(rate_dict))

        # get services of clinic selected by user
        user_services = Service.query.filter_by(clinic_id=user_clinic_id).first()
        
        print(user_services)
     

        return render_template('/show_services_rates.html', rate=user_clinic.rate_data, rate_dict=rate_dict, clinic_name=user_clinic_name,

                                 clinic_address=user_clinic_address, latitude=latitude, longitude=longitude, user_services=user_services)


    else: 
        flash("Sorry, no information about this clinic found.")
        redirect('/get-state-city')

                                        

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")




