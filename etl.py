# python modules
import pymysql
import pyodbc
from datetime import datetime


def etl(query, source_cnx, target_cnx):
    # extract data from source db

    source_cursor = source_cnx.cursor()
    start_time = datetime.now()
    source_cursor.execute(query.extract_query)
    data = source_cursor.fetchall()
    source_cursor.close()
    # -------QQ:
    # It is good to catch and log duration for getting the data from source
    # -------

    # load data into warehouse db
    if data:
        # --------------QQ:
        # Is this a good model to use between SET or PROCEDURAL operation
        # https://www.codeproject.com/Articles/34142/Understanding-Set-based-and-Procedural-approaches
        # --------------
        target_cursor = target_cnx.cursor()
        # target_cursor.execute("USE {}".format(datawarehouse_name))
        target_cursor.executemany(query.load_query, data)
        target_cnx.commit()
        # -------QQ:
        # Measure duration elapsed in milliseconds for Target write operation
        # So that you know where you are spending mode of your time
        # -------        
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
    # -------QQ:
    # Check for input params are not null
    # Throw specic err so you know which input is not valid
    # -------    
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
    # -------QQ:
    # You don't want to throw exception? Why string return value?
    # I haven't done Python and more of a learning question
    # -------
    
    # loop through sql queries
    for query in queries:
        etl(query, source_cnx, target_cnx)

    # close the source db connection
    # -------QQ:
    # After closing the cursor, can't immed. close source connection?
    # Do you have to keep it open until Target write Op. is complete?
    # -------
    source_cnx.close()
