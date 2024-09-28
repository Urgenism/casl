import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Keep this secret!
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'your_username')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'your_password')
    MYSQL_DB = os.getenv('MYSQL_DB', 'your_database')
