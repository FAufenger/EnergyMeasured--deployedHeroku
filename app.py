# # import necessary libraries

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import *
# from flask_migrate import Migrate
# from models import db, Percent

# metadata = MetaData()

import numpy as np

import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import ( Flask,
                    render_template,
                    jsonify,
                    request,
                    redirect)

###################
# Database Setup
###################
# Connect to local database

# Adding passcode for postgres
#code_source_passcode = open('/Users/Richa/Desktop/Files/SQL_private_connect.py') 
# Add you password here
#code_source_passcode = open('/Users/......./SQL_private_connect.py') 
#sql_private_connect = code_source_passcode.read()
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
#app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{sql_private_connect}@localhost:5432/Energy_DB'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///US_Energy_DB.sqlite'
# Remove tracking modifications
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#migrate = Migrate(app, db)

#db = SQLAlchemy(app)





# reflect an existing database into a new model
Base = automap_base()

# Create engine
engine = create_engine("sqlite:///US_Energy_DB.sqlite")

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#Classes is part of mapping and is required
Percent = Base.classes.us_percentage


###################
# Flask Setup
###################

app = Flask(__name__)


###################
# Create Routes
###################

# create route that renders index.html template
@app.route("/")
def index():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Percent.State).all()

    session.close()

    # Convert list of tuples into normal list
    all_states = list(np.ravel(results))

    return render_template('index.html', all_states = all_states)
    #return jsonify(pet_data)



@app.route("/api/data")

def statePercent():
    session = Session(engine)
    
    results = session.query(Percent.State, Percent.Nuclear,Percent.Coal,Percent.Natural_Gas,Percent.Petroleum,Percent.Hydro,Percent.Geothermal,Percent.Solar_PV,Percent.Wind,Percent.Biomass_and_Other).all()
    #results = session.query(us_percentage.STATE).all()
    session.close()
    
    # Getting each percentage in a a liat 
    Nuclear = [result[1] for result in results]
    Coal = [result[2] for result in results]
    Natural_Gas = [result[3] for result in results]
    Petroleum = [result[4] for result in results]
    Hydro = [result[5] for result in results]
    Geothermal = [result[6] for result in results]
    Solar_PV = [result[7] for result in results]
    Wind = [result[8] for result in results]
    Biomass_and_Other = [result[9] for result in results]

    # Value for first state
    values = Nuclear[0],Coal[0],Natural_Gas[0],Petroleum[0],Hydro[0],Geothermal[0],Solar_PV[0],Wind[0],Biomass_and_Other[0]
            

    result_percent_data = [{
        "type": "pie",
        "showlegend": "false",
        "rotation": 0,
        "textinfo": "text",
        "textposition": "inside",
        "values":[values],
        "text": ["0","1","2","3","4","5","6","7","8"],
        "hoverinfo": "skip",
        "marker": { 
            "colors": ["#ffd300", "#d21404", "#a0d080", "#90c070", "#80b060", "#70a050", "#609040", "#508030", "#407030" ],
            "labels": ["NA","0", "1", "2", "3","4","5","6","7"],
            "hoverinfo": "skip" 
        },
        "title": {"text": "<b>Percentage Energy Usage</b> <br> Per State",
                "font": { "size": 18} },
    }]
    
    return jsonify(result_percent_data)

# def findData():
#     find = 'us_percentage'
#     percent = db.session.query(find)
#     for state in percent:
#         print(state.STATE)
    
#     # table_name_string = request.get_json().get('us_percentage')
#     # selected_table = db.Table(table_name_string, metadata, autoload=True)
#     # query = selected_table.select()
#     # print(query)

#     # Return the template with the teams list passed in
#     #return render_template('index.html', percent=percent)
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)



# @app.route('/api/data2', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
     
#     if request.method == 'POST':
#         state = request.form['name']
#         year = request.form['age']
#         new_user = InfoModel(name=name, age=age)
#         db.session.add(new_user)
#         db.session.commit()
#         return f"Done!!"





# Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         pet = Pet(name=name, lat=lat, lon=lon)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")

