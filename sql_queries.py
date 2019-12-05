mysql_extract = ('''
  SELECT * FROM roxy r WHERE r.bookinginfoid > (SELECT l.highest_id FROM log_table l WHERE l.job_name='roxy' AND job_status='success' ORDER BY l.batch_id DESC LIMIT 1) LIMIT 5
''')

mysql_insert = ('''
  INSERT INTO roxy_datawarehouse (bookinginfoid, userid, usersessionid, movieid, moviename, genre, language, cityid, cinemaid, cinemaname, screenname, rating, bookingid, vistabookingno, vistatransno, sessionid, noofseats, showdate, showtime, ticketamount, foodamount, totalamount, bookingdate, seatinfo, tickettypecode, ticketdescription, vistastatus, recheckvistastatus, pgcross, pgstatus, refundstatus, emailstatus, smsstatus, recheckemailstatus, rechecksmsstatus, seatdetails, fooddesc, PaymentMessage, VistaRecheckMessage, SMSResponse, Platform, offeramount, couponapplied, pgtoken, cardnumber, resendcount, offerno, offertype, offeravailable, vatavailable, vatvalue, vatpercentage, pgcrosstime, pgresponsetime, pgsourcefrom, pgresponse, whatnewtype, PaymentMethod, gccardnumber, gcbalance, gcafterbalance,	gcpayment, Partialamount, screenid, experience,	DiscountAmount,	currentbalance,	beforebalance, ticketdiscount,	fnbdiscount, loyaltytier, EarnedPoint, ReedemPoint, Type)
  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  
''')

# exporting queries
class SqlQuery:
  def __init__(self, columns_check, extract_query, load_query):
    self.columns_check = columns_check
    self.extract_query = extract_query
    self.load_query = load_query
    
# create instances for SqlQuery class
mysql_query = SqlQuery(mysql_columns_check, mysql_extract, mysql_insert)

# store as list for iteration
mysql_queries = [mysql_query]
