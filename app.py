# # import necessary libraries
# #import os
# from flask import ( Flask,
#                     render_template,
#                     jsonify,
#                     request,
#                     redirect)

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import *
# from flask_migrate import Migrate
# from models import db, Percent

# metadata = MetaData()

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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

    return jsonify(all_states)


    # percentDB = 'SELECT * FROM us_percentage'
    # #percentDB = 'us_percentage'
    # #percentDB = 'State'
    # percent = db.session.query(percentDB)
    # # for state in percent:
    # #     print(state.State)
    # return render_template("index.html", percent=percent)
    

    # # Return the template with the teams list passed in
    # return render_template('index.html', percent=percent)
    # #return render_template("index.html")


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


# @app.route("/api/data")

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





    
### Do I need to put it into a json format?? ##
#def pals():
    # result_percent = db.session.query('select * from us_percentage', con=engine)
    #results = db.session.query(us_percentage.STATE).all()

    # hover_text = [result[0] for result in results]
    # lat = [result[1] for result in results]
    # lon = [result[2] for result in results]

    # result_percent_data = [{
    #     "type": "scattergeo",
    #     "locationmode": "USA-states",
    #     "lat": lat,
    #     "lon": lon,
    #     "text": hover_text,
    #     "hoverinfo": "text",
    #     "marker": {
    #         "size": 50,
    #         "line": {
    #             "color": "rgb(8,8,8)",
    #             "width": 1
    #         },
    #     }
    # }]
    
#    return jsonify(results)


