import mysql.connector
from typing import Dict, Any, Optional, List
from data_eating_interfaces.IResourceRepository import IResourceRepository

class MysqlResourceRepository(IResourceRepository):
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
    
    def create(self, data: Any) -> Any:
        """Insert data into database."""
        cursor = self.connection.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO resources ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(data.values()))
        self.connection.commit()
        return cursor.lastrowid
    
    def read(self, id: Any) -> Optional[Any]:
        """Retrieve data by ID."""
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM resources WHERE id = %s", (id,))
        return cursor.fetchone()
    
    def update(self, id: Any, data: Any) -> Optional[Any]:
        """Update data by ID."""
        cursor = self.connection.cursor()
        set_clause = ', '.join([f"{k} = %s" for k in data.keys()])
        query = f"UPDATE resources SET {set_clause} WHERE id = %s"
        cursor.execute(query, list(data.values()) + [id])
        self.connection.commit()
        return cursor.rowcount > 0
    
    def delete(self, id: Any) -> bool:
        """Delete data by ID."""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM resources WHERE id = %s", (id,))
        self.connection.commit()
        return cursor.rowcount > 0
    
    def list_all(self) -> List[Any]:
        """Retrieve all records."""
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM resources")
        return cursor.fetchall()
