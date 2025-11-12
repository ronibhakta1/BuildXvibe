from sqlalchemy import create_engine
from dotenv import load_dotenv      

load_dotenv()


engine = create_engine(DB_URL, echo=True)