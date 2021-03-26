from flask_sqlalchemy import SQLAlchemy
#import datetime

db = SQLAlchemy()

## First Table ##
class Percent(db.Model):
    __tablename__ = 'us_percentage'

    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(128))
    Nuclear = db.Column(db.Float)
    Coal = db.Column(db.Float)
    NaturalGas = db.Column(db.Float)
    Petroleum = db.Column(db.Float)
    Hydro = db.Column(db.Float)
    Geothermal = db.Column(db.Float)
    SolarPV = db.Column(db.Float)
    Wind = db.Column(db.Float)
    BiomassOther = db.Column(db.Float)


    def __init__(self, YEAR, STATE, TYPE_OF_PRODUCER, ENERGY_SOURCE, GENERATION_Mwh):
        self.State = State
        self.Nuclear = Nuclear
        self.Coal = Coal
        self.NaturalGas = NaturalGas
        self.Petroleum = Petroleum
        self.Hydro = Hydro
        self.Geothermal = Geothermal
        self.SolarPV = SolarPV
        self.Wind = Wind
        self.BiomassOther = BiomassOther

   def __repr__(self):
        return f"{self.State}:{self.Nuclear}:{self.Coal}: 
                {self.NaturalGas}:{self.Petroleum}:
                {self.Hydro}:{self.Geothermal}:{self.SolarPV}:
                {self.Wind}:{self.BiomassOther}:"



State,Nuclear,Coal,NaturalGas,Petroleum,Hydro,Geothermal,SolarPV,Wind,BiomassOther


## Second Table##

#class BaseModel(db.Model):
#     """Base data model for all objects"""
#     __abstract__ = True

#     def __init__(self, *args):
#         super().__init__(*args)

#     def __repr__(self):
#         """Define a base way to print models"""
#         return '%s(%s)' % (self.__class__.__name__, {
#             column: value
#             for column, value in self._to_dict().items()
#         })
#     def json(self):
#         """
#                 Define a base way to jsonify models, dealing with datetime objects
#         """
#         return {
#             column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
#             for column, value in self._to_dict().items()
#         }


