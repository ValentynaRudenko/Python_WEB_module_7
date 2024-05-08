from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///university.db')
Session = sessionmaker(bind=engine)
session = Session()
