# variables
from db_credentials import datawarehouse_db_config, sqlserver_db_config, mysql_db_config, sqlite_db_config
from sql_queries import mysql_queries
#from etl import start_time, end_time
from variables import *
# methods
from etl import etl_process
import sqlite3
import pymysql


def main():
  print('starting etl')
	
  # establish connection for target database (sql-server)
  target_cnx = pymysql.connect(**datawarehouse_db_config)
	
  # loop through credentials

  # sqlite
  #for config in sqlite_db_config:
  #  try:
  #    print("loading db: " + config['database'])
  #    etl_process(sqlite_queries, target_cnx, config, 'sqlite')
  #  except Exception as error:
  #    print("etl for {} has error".format(config['database']))
  #    print('error message: {}'.format(error))
  #    tcur = target_cnx.cursor()
  #    error_insert = ('''INSERT INTO log_table (`job_name`, `failure_reason`) VALUES (%s, %s)''')
  #    error_params = ('roxy', str(error))
  #    tcur.execute(error_insert, error_params)
  #    target_cnx.commit()
  #    continue

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
      target_cnx.commit()
      continue

	
  target_cnx.close()

if __name__ == "__main__":
  main()