import psycopg2
from psycopg2 import pool, Error
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
import logging
from config import DB_CONFIG

logger = logging.getLogger(__name__)

class DatabaseManager:
    _instance = None
    _pool = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._pool is None:
            self._initialize_pool()
    
    def _initialize_pool(self):
        try:
            self._pool = psycopg2.pool.ThreadedConnectionPool(
                2, 20,
                host=DB_CONFIG.host,
                port=DB_CONFIG.port,
                database=DB_CONFIG.database,
                user=DB_CONFIG.user,
                password=DB_CONFIG.password
            )
        except Error as e:
            logger.error(f"خطأ: {e}")
            raise
    
    @contextmanager
    def get_cursor(self):
        conn = self._pool.getconn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor
            conn.commit()
        except Error as e:
            conn.rollback()
            raise
        finally:
            cursor.close()
            self._pool.putconn(conn)
    
    def execute_query(self, query, params=None):
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description:
                return cursor.fetchall()
            return []
    
    def execute_one(self, query, params=None):
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description:
                return cursor.fetchone()
        return None

db = DatabaseManager()

def init_database():
    import os
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            with db.get_cursor() as cursor:
                cursor.execute(f.read())
        return True
    except Exception as e:
        logger.error(f"خطأ: {e}")
        return False
