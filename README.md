# ART(Assited Reproductive Technology) Guidelines
ART Guidelines is a full-stack web application that allows couples with fertility problems to search for a list of all fertility clinics along with their full address in a particular city. Once users click on a clinic, they can see  each clinic's most current success rates based on different patient age groups,  the types of embryo transfer they have received and outcomes.  This app also displays probabilities for singleton and multiple live births in the form of charts so the data are more readable for users.  With ART Guidelines, fertility treatments are a lot less stressful.
ART Guidelines integrates data and features from cdc.gov, Google Map and Places API.

Access

Tech Stack
Frontend: Bootstrap, HTML, CSS, JavaScript, Jinja, jQuery<br>
Backend: Python, Flask, PostgreSQL, SQLAlchemy<br>
API: Google Maps API, Places API

Demo
Users can search for list of all fertility clinics in a particular city 
![](READMEgifs/homepage.gif)


Once the list appears, users can click on each clinic's name to view its data. The locations of all clinics are also displayed on a map.

![](READMEgifs/show_list.gif)


Users can see full address of a particular clinic and its location on a map. They can also see clinic profile, services it is providing, and success rates, which are divided into groups based on patient age groups, types of embryo transfers, and outcomes. The data are displayed in the form of both tables and charts.

![](READMEgifs/show_rates.gif)


The most exciting feature of this app is the ability to provide data that users can rely on since the data come from the most current Center for Disease Control and Prevention's fertility rate report.



Future Features
* Allowing users to search for clinics by zipcode
* Users can rate each clinic and save their ratings in their accounts

