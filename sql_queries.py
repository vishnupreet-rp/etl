firebird_extract = ('''
  SELECT fbd_column_1, fbd_column_2, fbd_column_3
  FROM fbd_table;
''')

firebird_insert = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (%s, %s, %s)  
''')

firebird_extract_2 = ('''
  SELECT fbd_column_1, fbd_column_2, fbd_column_3
  FROM fbd_table_2;
''')

firebird_insert_2 = ('''
  INSERT INTO table_2 (column_1, column_2, column_3)
  VALUES (%s, %s, %s)  
''')

sqlserver_extract = ('''
  SELECT sqlserver_column_1, sqlserver_column_2, sqlserver_column_3
  FROM sqlserver_table
''')

sqlserver_insert = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (%s, %s, %s)  
''')

mysql_columns_check = ('''DESC roxy''')

mysql_extract = ('''
  SELECT * FROM roxy r WHERE r.bookinginfoid > (SELECT l.highest_id FROM log_table l WHERE l.job_name='roxy' AND job_status='success' ORDER BY l.batch_id DESC LIMIT 1) LIMIT 5
''')

mysql_insert = ('''
  INSERT INTO roxy_datawarehouse (bookinginfoid, userid, usersessionid, movieid, moviename, genre, language, cityid, cinemaid, cinemaname, screenname, rating, bookingid, vistabookingno, vistatransno, sessionid, noofseats, showdate, showtime, ticketamount, foodamount, totalamount, bookingdate, seatinfo, tickettypecode, ticketdescription, vistastatus, recheckvistastatus, pgcross, pgstatus, refundstatus, emailstatus, smsstatus, recheckemailstatus, rechecksmsstatus, seatdetails, fooddesc, PaymentMessage, VistaRecheckMessage, SMSResponse, Platform, offeramount, couponapplied, pgtoken, cardnumber, resendcount, offerno, offertype, offeravailable, vatavailable, vatvalue, vatpercentage, pgcrosstime, pgresponsetime, pgsourcefrom, pgresponse, whatnewtype, PaymentMethod, gccardnumber, gcbalance, gcafterbalance,	gcpayment, Partialamount, screenid, experience,	DiscountAmount,	currentbalance,	beforebalance, ticketdiscount,	fnbdiscount, loyaltytier, EarnedPoint, ReedemPoint, Type)
  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  
''')

sqlite_extract = ('''
  SELECT * FROM roxy
''')

sqlite_insert = ('''
  INSERT INTO datawarehouse_db (bookinginfoid, userid, usersessionid, movieid, moviename, genre, language, cityid, cinemaid, cinemaname, screenname, rating, bookingid, vistabookingno, vistatransno, sessionid, noofseats, showdate, showtime, ticketamount, foodamount, totalamount, bookingdate, seatinfo, tickettypecode, ticketdescription, vistastatus, recheckvistastatus, pgcross, pgstatus, refundstatus, emailstatus, smsstatus, recheckemailstatus, rechecksmsstatus, seatdetails, fooddesc, PaymentMessage, VistaRecheckMessage, SMSResponse, Platform, offeramount, couponapplied, pgtoken, cardnumber, resendcount, offerno, offertype, offeravailable, vatavailable, vatvalue, vatpercentage, pgcrosstime, pgresponsetime, pgsourcefrom, pgresponse, whatnewtype, PaymentMethod, gccardnumber, gcbalance, gcafterbalance,	gcpayment, Partialamount, screenid, experience,	DiscountAmount,	currentbalance,	beforebalance, ticketdiscount,	fnbdiscount, loyaltytier, EarnedPoint, ReedemPoint, Type)
  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
''')

# exporting queries
class SqlQuery:
  def __init__(self, columns_check, extract_query, load_query):
    self.columns_check = columns_check
    self.extract_query = extract_query
    self.load_query = load_query
    
# create instances for SqlQuery class
#fbd_query = SqlQuery(firebird_extract, firebird_insert)
#fbd_query_2 = SqlQuery(firebird_extract_2, firebird_insert_2)
#sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)
mysql_query = SqlQuery(mysql_columns_check, mysql_extract, mysql_insert)
#sqlite_query = SqlQuery(sqlite_extract, sqlite_insert)

# store as list for iteration
#fbd_queries = [fbd_query, fbd_query_2]
#sqlserver_queries = [sqlserver_query]
mysql_queries = [mysql_query]
#sqlite_queries = [sqlite_query]