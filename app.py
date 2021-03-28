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
Percent_US = Base.classes.us_percentage
Generation_US= Base.classes.us_generation
No_Electricity_World = Base.classes.world_no_electricity
Generation_World = Base.classes.world_generation
Consumption_World = Base.classes.world_consumption


app = Flask(__name__)

 
@app.route("/")
def home():

     # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all states"""
    # Query all passengers
    results = session.query(Percent_US.State).all()
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
    results = session.query(Percent_US.State, Percent_US.Nuclear,Percent_US.Coal,Percent_US.Natural_Gas,Percent_US.Petroleum,Percent_US.Hydro,Percent_US.Geothermal,Percent_US.Solar_PV,Percent_US.Wind,Percent_US.Biomass_and_Other).all()
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



@app.route("/api/data2")
def stateGeneration():
    session2 = Session(engine)
    results2 = session2.query(Generation_US.year, Generation_US.coal, Generation_US.natural_gas, Generation_US.nuclear, Generation_US.renewables, Generation_US.petroleum_and_other).all()
    session2.close()
    
    test2 = list(np.ravel(results2))
    
       
    return jsonify(results2)



@app.route("/api/data3")
def NoElectricityWorld():
    session3 = Session(engine)
    results3 = session3.query(No_Electricity_World.Country, No_Electricity_World.Code, No_Electricity_World.Year, No_Electricity_World.Number_people_without_electricity).all()
    session3.close()
    
    test3 = list(np.ravel(results3))
       
    return jsonify(results3)




@app.route("/api/data4")
def worldGeneration():
    session4 = Session(engine)
    results4 = session4.query(Generation_World.Country, Generation_World.Code, Generation_World.Year, Generation_World.Solar, Generation_World.Wind, Generation_World.Hydro, Generation_World.Geo_Biomass_Other).all()
    session4.close()
    
    test4 = list(np.ravel(results4))
       
    return jsonify(results4)




@app.route("/api/data5")
def worldConsumption():
    session5 = Session(engine)
    results5 = session5.query(Consumption_World.Country, Consumption_World.Code, Consumption_World.Year, Consumption_World.Traditional_biomass, Consumption_World.Hydro, Consumption_World.Solar, Consumption_World.Wind,  Consumption_World.Geo_Biomass_Other).all()
    session5.close()
    
    test5 = list(np.ravel(results5))
       
    return jsonify(results5)



if __name__ == "__main__":
    app.run(debug=True)