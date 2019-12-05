from variables import datawarehouse_name

# sql-server (target db, datawarehouse)
datawarehouse_db_config = {
    'user': 'root',
    'password': 'vishnu',
    'host': 'localhost',
    'database': 'transactions',
  }


# sqlite
sqlite_db_config = [
  {
#    'user': 'your_user_1',
#    'password': 'your_password_1',
#    'host': r'C:\Users\vishn\roxy.db',
    'database': r'C:\Users\vishn\roxy.db',
  }
]

# sql-server (source db)
sqlserver_db_config = [
  {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'your_sql_server',
    'database': 'db1',
    'user': 'your_db_username',
    'password': 'your_db_password',
    'autocommit': True,
  }
]

# mysql
mysql_db_config = [
  {
    'user': 'root',
    'password': 'vishnu',
    'host': 'localhost',
    'database': 'transactions',
  }
#  {
#    'user': 'your_user_2',
#    'password': 'your_password_2',
#    'host': 'db_connection_string_2',
#    'database': 'db_2',
#  },
]

# firebird
fdb_db_config = [
  {
    'dsn': "/your/path/to/source.db",
    'user': "your_username",
    'password': "your_password",
  }
]
