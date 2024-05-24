from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker


load_dotenv()
DB_ADDRESS = os.getenv('DB_ADDRESS')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}/{DB_NAME}"
engine = create_engine(url)
Session = sessionmaker(bind=engine)

def execute_query(query: str):
    session = Session()
    result = session.execute(text(query))
    session.commit()
    session.close()
    return result
