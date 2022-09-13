from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:toledin1@localhost/db_F1"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

df_circuits= pd.read_csv('https://raw.githubusercontent.com/toledojm/PI01_DATA03/main/Datasets/circuits.csv')
with engine.connect() as conn, conn.begin():
    df_circuits.to_sql('circuit', conn, if_exists='append', index=False)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()