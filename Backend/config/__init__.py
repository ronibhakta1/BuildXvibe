from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent  
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
	load_dotenv(dotenv_path=str(ENV_PATH))
else:
	load_dotenv()
E2B_KEY = os.getenv("E2B_API_KEY", "")

__all__ = ["E2B_KEY"]