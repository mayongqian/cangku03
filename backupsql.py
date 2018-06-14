import pymysql
import os
connect = pymysql.connect(       
    user="root",
    password="1234",
    host="127.0.0.1",
    db="project",
    charset="utf8",
    port=3306
    )
conn = connect.cursor()
key="1234"
path = "/var/lib/jenkins/Backupfile"
os.system("mysql -u root -p%s keshe project> %s.sql" % (key,path))
