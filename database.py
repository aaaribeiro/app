from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2:postgres://vxjrxgdmrsrtrm:23f4c32e71081e7fe9213dbd8c9592a8aa8371a73db14c4e087de19374c89f0c@ec2-3-231-40-72.compute-1.amazonaws.com:5432/dbv392m50ekkf4"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
