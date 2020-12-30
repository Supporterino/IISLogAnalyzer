import sqlalchemy as db

class database:
    def __init__(self):
        engine: db._engine.Engine = db.create_engine('sqlite:///logs.db', echo=True)
        connection = engine.connect()
        metadata = db.MetaData()