# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:18:44 2022

@author: scchou
"""
import datetime
import pymysql
import os
import requests
from datetime import date, datetime, timedelta
os.chdir('D:\\Chou\Python\B2202')



lasttime = []#time
ST_NO = []
M10 = []
H1 = []
H3 = []
H6 = []
H12 = []
H24 = []

db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='50770329',
                     database='rainbox')
cursor = db.cursor()


requests.packages.urllib3.disable_warnings()
r = requests.get("https://www.eocmap.gov.taipei/eocmap/Meter/RainStationInfo", verify=False)
list_of_dicts = r.json()

for i in range(len(list_of_dicts)):
    lasttime = str(datetime.strptime(str(list_of_dicts[i]['DATE']), '%Y-%m-%dT%H:%M:%S'))
    ST_NO = list_of_dicts[i] ['ST_NO']
    M10 = list_of_dicts[i] ['M10']
    H1 = list_of_dicts[i] ['H1']
    H3 = list_of_dicts[i] ['H3']
    H6 = list_of_dicts[i] ['H6']
    H12 = list_of_dicts[i] ['H12']
    H24 = list_of_dicts[i] ['H24']

    sql = f"""
        INSERT INTO taipei_rain(id,
        time, ST_NO, M10 ,H1 ,H3 , H6, H12, H24)
        VALUES (NULL, '{lasttime}', '{ST_NO}', {M10}, {H1}, {H3}, {H6},{H12},{H24})"""

    cursor.execute(sql)
    db.commit()

db.close()

#https://www.eocmap.gov.taipei/eocmap/Meter/RainStationBase 台北雨量站資料

#SELECT * FROM taipei_rain WHERE time BETWEEN 20221123 AND 20221126 AND st_no = 317
