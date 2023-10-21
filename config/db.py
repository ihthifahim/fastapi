from sqlalchemy import create_engine, MetaData


DB_URL = "mysql+pymsql:://root@localhost:3306/fastapidb"

engine = create_engine(
    DB_URL
)

meta = MetaData()
conn = engine.connect()