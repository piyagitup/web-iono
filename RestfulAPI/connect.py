import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='remotemysql.com',
                                       port='3306',
                                       database='fvpnSn9xtp',
                                       user='fvpnSn9xtp',
                                       password='x6DdkN6mXz')
        if conn.is_connected():
            print('Connected to MySQL database')
        mycursor = conn.cursor()
        # sql = "insert into ap(ap,level_ap) value(%s,%s)" 
        # val=(2 , "น้อย")
   
        # mycursor.execute(sql,val)
        # conn.commit(); 
    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()