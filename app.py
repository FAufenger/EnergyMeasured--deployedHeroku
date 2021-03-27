# from models import create_classes
import os
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify, request, url_for



# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()

# Create engine
engine = create_engine("sqlite:///US_Energy_DB.sqlite")

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#Classes is part of mapping and is required
Percent = Base.classes.us_percentage

app = Flask(__name__)

 
@app.route("/")
def home():

     # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Percent.State).all()

    session.close()

    # Convert list of tuples into normal list
    all_states = list(np.ravel(results))
    return render_template("index.html")

@app.route("/option1/")
def option1():
    return render_template("option1.html")

@app.route("/option2/")
def option2():
    return render_template("option2.html")

@app.route("/option3/")
def option3():
    return render_template("map.html")

@app.route("/api/data")
def statePercent():
    session = Session(engine)
    
    results = session.query(Percent.State, Percent.Nuclear,Percent.Coal,Percent.Natural_Gas,Percent.Petroleum,Percent.Hydro,Percent.Geothermal,Percent.Solar_PV,Percent.Wind,Percent.Biomass_and_Other).all()
    #results = session.query(us_percentage.STATE).all()
    session.close()
    
    # # Getting each percentage in a a liat 
    # Nuclear = [result[1] for result in results]
    # Coal = [result[2] for result in results]
    # Natural_Gas = [result[3] for result in results]
    # Petroleum = [result[4] for result in results]
    # Hydro = [result[5] for result in results]
    # Geothermal = [result[6] for result in results]
    # Solar_PV = [result[7] for result in results]
    # Wind = [result[8] for result in results]
    # Biomass_and_Other = [result[9] for result in results]

    # # Value for first state
    # values = Nuclear[0],Coal[0],Natural_Gas[0],Petroleum[0],Hydro[0],Geothermal[0],Solar_PV[0],Wind[0],Biomass_and_Other[0]
            

    result_percent_data = [{
        "type": "pie",
        "showlegend": False,
        "rotation": 0,
        "textinfo": "text+percent",
        "textposition": "inside",
        "values":results[0][1:],
        "text": ["Nuclear","Coal","Natural Gas","Petroleum","Hydro","Geothermal","Solar-PV","Wind","Biomass/ Other"],
        "hoverinfo": "skip",
        "autopct": '%1.1f%%', 
        "marker": { 
            "colors": ["#347C17", "#6960EC", "#43C6DB", "#3EA055", "#FFFF00", "#FF7F50", "#4B0082", "#C48189", "#B93B8F"],
            "labels": ["Nuclear","Coal","Natural Gas","Petroleum","Hydro","Geothermal","Solar-PV","Wind","Biomass/ Other"],
            "hoverinfo": "skip" 
        },
        "title": {"text": f'<b>Percentage Energy Usage</b> <br> {results[0][0]}',
                "font": { "size": 18} },
    }]
    
    return jsonify(result_percent_data)

if __name__ == "__main__":
    app.run(debug=True)