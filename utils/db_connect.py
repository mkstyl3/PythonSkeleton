import sqlalchemy

from config.database import *
from sqlalchemy.sql import *
from sqlalchemy.orm import sessionmaker


# sqlalchemy.__version__

connection = None

try:
    engine = sqlalchemy.create_engine("mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}?charset=utf8".format(db_user=DB_USER,db_pass=DB_PASS,db_host=DB_HOST, db_name=DB_NAME))
    session = sessionmaker(bind=engine)
    # connection = engine.raw_connection().cursor()
    connection = engine.connect()
except Exception:
    raise Exception('No connection to database')

