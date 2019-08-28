from sqlalchemy import create_engine, __version__, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DB_connection:
    def __init__(self):
        self.engine = create_engine('sqlite:///database/database.db', echo=True)
        self.session = (sessionmaker(bind=self.engine))()
        self.version = __version__


    def create_schema(self):
        Base.metadata.create_all(self.engine)



class LogEntry(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    time = Column(String)
    s_ip = Column(String)
    cs_method = Column(String)
    cs_uri_stem = Column(String)
    cs_uri_query = Column(String)
    s_port = Column(String)
    cs_username = Column(String)
    c_ip = Column(String)
    user_agent = Column(String)
    referer = Column(String)
    sc_status = Column(String)
    sc_substatus = Column(String)
    sc_win32_status = Column(String)
    cs_bytes = Column(String)
    time_taken = Column(String)
    timestamp = Column(String)