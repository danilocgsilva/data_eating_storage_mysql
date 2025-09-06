# Data Eating Storage MySQL

A MySQL storage solution for data eating operations.

## Installation

```bash
pip install data-eating-storage-mysql
```

## Usage

```python
from data_eating_storage_mysql import MySQLStorage

storage = MySQLStorage(
    host="localhost",
    user="username",
    password="password",
    database="mydb"
)

storage.store_data("mytable", {"column1": "value1", "column2": "value2"})
```