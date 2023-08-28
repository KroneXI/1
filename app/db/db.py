from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def create_tables(self):
        self.Base.metadata.create_all(bind=self.engine)

    def execute(self, func):
        db = self.SessionLocal()
        try:
            result = func(db)
            db.commit()
            return result
        finally:
            db.close()