import psycopg2
from config.config import DB_SETTINGS

def connect_db():
    return psycopg2.connect(**DB_SETTINGS)
