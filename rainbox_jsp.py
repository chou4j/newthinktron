# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:18:44 2022

@author: scchou
"""

import dropbox
import datetime
import pymysql
import os

os.chdir('D:\\Chou\Python\B2202')


token = 'v-91Fc0MwBAAAAAAAAAO6znHHc96sV8CLLyqk04EECHOrAImvuDKhyWB3FpegJaf'
dbx = dropbox.Dropbox(token)

with open("JSP_RTValue.txt", "wb") as f:
    metadata, res = dbx.files_download(path="/thinktron/JSP_RTValue.txt")
    f.write(res.content)

path = 'D:/Chou/Python/B2202/JSP_RTValue.txt'
f = open(path, 'r')
print(f.read())
f.seek(0)
result = []
for line in f.readlines():
    line=line.replace(",",",").replace("\n","")
    line.split(', ', 1)
    result.append(line)
f.close()
print(result)


lasttime = []#time
log1 = []
log2 = []
log3 = []
log4 = []
log5 = []#雨量

lastdata = result[len(result)-1].split(',')
#lasttime = lastdata[0]
lasttime = str(datetime.datetime.strptime(str(lastdata[0]), '%Y/%m/%d %H:%M:%S '))
log1 = lastdata[1]
log2 = lastdata[2]
log3 = lastdata[3]
log4 = lastdata[4]
log5 = lastdata[5]



db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='50770329',
                     database='rainbox')

cursor = db.cursor()


#sql = ' UNION ALL' if i > 0 else ''
sql = f"""
        INSERT INTO taipei_jsp(id,
        time, log1, log2, log3, log4, log5)
        VALUES (NULL, '{lasttime}', {log1}, {log2}, {log3}, {log4}, {log5})"""

cursor.execute(sql)
db.commit()

db.close()





