# python modules
import pymysql
import pyodbc
from datetime import datetime
# import fdb
import sqlite3
# variables
#from variables import datawarehouse_name

def source_fields_check(query, source_cnx, target_cnx):
    source_cursor = source_cnx.cursor()
    source_cursor.execute(query.columns_check)
    print([col[0] for col in source_cursor.fetchall()])


def etl(query, source_cnx, target_cnx):
    # extract data from source db

    source_cursor = source_cnx.cursor()
    start_time = datetime.now()
    source_cursor.execute(query.extract_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    # load data into warehouse db
    if data:
        target_cursor = target_cnx.cursor()
        # target_cursor.execute("USE {}".format(datawarehouse_name))
        target_cursor.executemany(query.load_query, data)
        target_cnx.commit()
        end_time = datetime.now()
        print('data loaded to warehouse db')
        target_cursor.execute('''SELECT highest_id FROM log_table WHERE job_status='success' ORDER BY batch_id DESC LIMIT 1''')
        lowest_id = target_cursor.fetchone()
        lowest_id = lowest_id[0]
        target_cursor.execute('''SELECT bookinginfoid FROM roxy_datawarehouse ORDER BY id DESC LIMIT 1''')
        highest_id = target_cursor.fetchone()
        log_table_insert_query = ('''INSERT INTO log_table (`job_name`, `job_start_date`, `job_end_date`, 
        `lowest_id`, `highest_id`, `job_status`) VALUES (%s, %s, %s, %s, %s, %s)''')
        log_table_insert_params = ('roxy', start_time,
                              end_time, (lowest_id+1), highest_id, 'success')
        target_cursor.execute(log_table_insert_query, log_table_insert_params)
        target_cnx.commit()
        target_cursor.close()
    else:
        print('data empty')
        target_cursor = target_cnx.cursor()
        data_empty_insert = ('''INSERT INTO log_table (`job_name`, `job_start_date`, `job_status`, `failure_reason`) VALUES (%s, %s, %s, %s)''')
        data_empty_params = ('roxy', start_time, 'failed', 'data empty')
        target_cursor.execute(data_empty_insert, data_empty_params)
        target_cnx.commit()


def etl_process(queries, target_cnx, source_db_config, db_platform):
    # establish source db connection
    if db_platform == 'mysql':
        source_cnx = pymysql.connect(**source_db_config)
    elif db_platform == 'sqlserver':
        source_cnx = pyodbc.connect(**source_db_config)
    elif db_platform == 'firebird':
        source_cnx = fdb.connect(**source_db_config)
    elif db_platform == 'sqlite':
        source_cnx = sqlite3.connect(**source_db_config)
    else:
        return 'Error! unrecognised db platform'

    # loop through sql queries
    for query in queries:
        etl(query, source_cnx, target_cnx)

    # close the source db connection
    source_cnx.close()
