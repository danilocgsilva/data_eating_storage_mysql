"""MySQL storage implementation."""

import mysql.connector
from typing import Dict, Any, Optional


class MySQLStorage:
    """MySQL storage handler for data eating operations."""
    
    def __init__(self, host: str, user: str, password: str, database: str):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None
    
    def connect(self):
        """Establish database connection."""
        self.connection = mysql.connector.connect(**self.config)
    
    def disconnect(self):
        """Close database connection."""
        if self.connection:
            self.connection.close()
    
    def store_data(self, table: str, data: Dict[str, Any]) -> bool:
        """Store data in specified table."""
        if not self.connection:
            self.connect()
        
        cursor = self.connection.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        
        try:
            cursor.execute(query, list(data.values()))
            self.connection.commit()
            return True
        except Exception:
            self.connection.rollback()
            return False
        finally:
            cursor.close()