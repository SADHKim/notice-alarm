### get users' mail from database ###

import pymysql

### the function returns recievers list with database table name as params ###
def get_recievers(websiteName):
    
    conn = pymysql.connect(host='localhost', user='', passwd='', db='', charset='utf8')
    cursor = conn.cursor()
    
    sql = 'SELECT email FROM eamil_list WHERE website_name = ' + websiteName
    cursor.execute(sql)
    
    recieversList = cursor.fetchall()
    
    return recieversList