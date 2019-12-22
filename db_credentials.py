from variables import datawarehouse_name
# ---------QQ
# ---- Do not keep creds in source code
# ---------
# mysql (target db, datawarehouse)
datawarehouse_db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'transactions',
  }

# mysql
mysql_db_config = [
  {
    'user': 'root',
    'password': 'vishnu',
    'host': 'localhost',
    'database': 'transactions',
  }
