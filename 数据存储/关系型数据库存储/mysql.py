import pymysql

pymysql.install_as_MySQLdb()



db = pymysql.connect(
    host='192.168.14.91',
    user='root',
    password='mysql',
    port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8 ")
db.close()