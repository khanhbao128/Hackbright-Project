# ART(Assited Reproductive Technology) Guidelines
ART Guidelines is a full-stack web application that allows couples with fertility problems to search for a list of all fertility clinics along with their full address in a particular city. Once users click on a clinic, they can see  each clinic's most current success rates based on different patient age groups,  the types of embryo transfer they have received and outcomes.  This app also displays probabilities for singleton and multiple live births in the form of charts so the data are more readable for users.  With ART Guidelines, fertility treatments are a lot less stressful.
ART Guidelines integrates data and features from cdc.gov, Google Map and Places API.


Tech Stack
Frontend: Bootstrap, HTML, CSS, JavaScript, Jinja, jQuery<br>
Backend: Python, Flask, PostgreSQL, SQLAlchemy<br>
API: Google Maps API, Places API

## Setup/Installation

On local machine, go to directory where you want to work and clone ART Guidelines repository:
```
$ git clone https://github.com/khanhbao128/Hackbright-Project.git
```
Create a virtual environment in the directory:
```
$ virtualenv env
```
Activate virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Create database:
```
$ createdb rates
```
Create your database tables:
```
$ python3 model.py
```
Seed database
```
$ python3 seed.py
```

Create .gitignore file:
```
$ touch .gitignore
```
Access .gitignore file in terminal to ignore config.py file:
```
$ nano .gitignore
```
Run the app:
```
$ python3 server.py
```
Open localhost:5000 on browser.

Demo
Users can search for list of all fertility clinics in a particular city 
![2019-06-19 10 50 39](https://user-images.githubusercontent.com/46436967/59788226-1e19fe80-9280-11e9-8f68-9172ed556761.gif)

Once the list appears, users can click on each clinic's name to view its data. The locations of all clinics are also displayed on a map.

![](show_list_1.gif)


Users can see full address of a particular clinic and its location on a map. They can also see clinic profile, services it is providing, and success rates, which are divided into groups based on patient age groups, types of embryo transfers, and outcomes. The data are displayed in the form of both tables and charts.

![](show_rates_1.gif)


The most exciting feature of this app is the ability to provide data that users can rely on since the data come from the most current Center for Disease Control and Prevention's fertility rate report.



Future Features
* Allowing users to search for clinics by zipcode
* Users can rate each clinic and save their ratings in their accounts
