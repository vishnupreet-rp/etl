# import variables
from db_credentials import datawarehouse_db_config, sqlserver_db_config, mysql_db_config, sqlite_db_config
from sql_queries import mysql_queries
from variables import *
# import methods
from etl import etl_process
# import libraries
import pymysql


def main():
  print('starting etl')
	
  # establish connection with target database (mysql)
  target_cnx = pymysql.connect(**datawarehouse_db_config)
	
  # mysql
  for config in mysql_db_config:
    try:
      print("loading db: " + config['database'])
      etl_process(mysql_queries, target_cnx, config, 'mysql')
    except Exception as error:
      print("etl for {} has error".format(config['database']))
      print('error message: {}'.format(error))
      tcur = target_cnx.cursor()
      error_insert = ('''INSERT INTO log_table (`job_name`, `failure_reason`) VALUES (%s, %s)''')
      error_params = ('roxy', str(error))
      tcur.execute(error_insert, error_params)
    # -------QQ:
    # Based on my newbie understanding of Python, I think your  
    # target DB and your log DB are the same. It will be good to keep 
    # logs/telemetry on seperate DB. Let us discuss WHY?
    # -------	
      target_cnx.commit()
      continue

	
  target_cnx.close()

if __name__ == "__main__":
  main()
