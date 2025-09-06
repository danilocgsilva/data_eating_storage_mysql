# Data Eating Storage MySQL

A MySQL storage solution for data eating operations.

## Installation

```bash
pip install git+https://github.com/danilocgsilva/data_eating_storage_mysql.git
```

## Usage

First, the environment must have some system variables: 
* `DATABASE_PASSWORD`
* `DATABASE_USER`

, which is the self explanatory by its name.

Them, you can import the package in your system.

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