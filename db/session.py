from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from core.config import settings

# SQLALCHEMY_DATABASE_URL= settings.DATABASE_URL

engine = create_engine('postgresql://newuser:Bardock123$@127.0.0.1:5432/db_course')

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

print(SessionLocal)