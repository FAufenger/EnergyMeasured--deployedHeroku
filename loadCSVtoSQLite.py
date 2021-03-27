import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy import create_engine, MetaData, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float


csvfiles = ["./Resources/US/us_percentage.csv", "./Resources/US/annual_generation_US.csv"]
engine = create_engine("sqlite:///US_Energy_DB.sqlite")
conn = engine.connect()

###
# Use SQLAlchemy to model table schema
###
Base = declarative_base()


class PercentUS(Base):
    __tablename__ = 'us_percentage'

    id = Column(Integer, primary_key=True)
    State = Column(Text)
    Nuclear = Column(Integer)
    Coal = Column(Integer)
    Natural_Gas = Column(Integer)
    Petroleum = Column(Integer)
    Hydro = Column(Integer)
    Geothermal = Column(Integer)
    Solar_PV = Column(Integer)
    Wind = Column(Integer)
    Biomass_and_Other = Column(Integer)

class us_generation_power(Base):
    __tablename__ = 'us_generation'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    state = Column(Text)
    type_of_producer = Column(Text)
    energy_source = Column(Text)
    generation_mhw = Column(Integer)


    # def __repr__(self):
    #     return f"id={self.id}, name={self.title}"


Base.metadata.create_all(engine)
metadata = MetaData(bind=engine)
metadata.reflect()

###
# Use Pandas to read csv into a list of row objects
###
df = pd.read_csv(csvfiles[0], dtype=object)
percent_us_data = df.to_dict(orient='records')
###
df = pd.read_csv(csvfiles[1], dtype=object)
generation_us_data = df.to_dict(orient='records')

###
# Insert data into table using SQLAlchemy
###
percent_us_table = sqlalchemy.Table('us_percentage', metadata, PrimaryKeyConstraint('id'),
                            autoload=True, extend_existing=True)
generation_us_table = sqlalchemy.Table('us_generation', metadata, PrimaryKeyConstraint('id'),
                            autoload=True, extend_existing=True)

conn.execute(percent_us_table.delete())
conn.execute(percent_us_table.insert(), percent_us_data)

conn.execute(generation_us_table.delete())
conn.execute(generation_us_table.insert(), generation_us_data)
