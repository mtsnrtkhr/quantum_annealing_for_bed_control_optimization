# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# .env に設定した変数を取り出す
DWAVE_API_TOKEN = os.getenv('DWAVE_API_TOKEN')
