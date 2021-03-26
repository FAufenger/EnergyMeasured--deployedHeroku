# import necessary libraries
import os
from flask import ( Flask,
                    render_template,
                    jsonify,
                    request,
                    redirect)
from flask_sqlalchemy import SQLAlchemy

###################
# Flask Setup
###################

app = Flask(__name__)

###################
# Database Setup
###################
# Connect to local database
code_source_passcode = open('/Users/Richa/Desktop/Files/SQL_private_connect.py') 
# Add you password here
#code_source_passcode = open('/Users/......./SQL_private_connect.py') 

sql_private_connect = code_source_passcode.read()
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{sql_private_connect}@localhost:5432/Energy_DB'

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# NewDB CLASS = create_classes(db)


###################
# Create Routes
###################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["petName"]
        lat = request.form["petLat"]
        lon = request.form["petLon"]

        pet = Pet(name=name, lat=lat, lon=lon)
        db.session.add(pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")


@app.route("/api/data")
def pals():
    results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

    hover_text = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    pet_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(pet_data)


if __name__ == "__main__":
    app.run()
