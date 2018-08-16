from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()
engine = create_engine('sqlite:///catalog_database.db')
Base.metadata.drop_all(bind=engine)
print("Deleted")
