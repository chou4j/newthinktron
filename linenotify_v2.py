# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:00:49 2022

@author: scchou
"""
import requests
import datetime
import dropbox
import os

os.chdir("D:\\thinktron\B2202")

starttime = datetime.datetime.now()  #計算起始時間

token = 'xiCJk7f1ntt8L28fxsvK36KRprZ8fkPNk1s4MYdOD4M'
#和鐘哥的共同群組

#------------------LINE模組-------------------#
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
	
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

#------------------讀取dropbox數據-------------------#

dptoken = 'v-91Fc0MwBAAAAAAAAAO6znHHc96sV8CLLyqk04EECHOrAImvuDKhyWB3FpegJaf'
dbx = dropbox.Dropbox(dptoken)

with open("DTL_RTValue.txt", "wb") as f:
    metadata, res = dbx.files_download(path="/thinktron/DTL_RTValue.txt")
    f.write(res.content)

path = 'D:/thinktron/b2202/DTL_RTValue.txt'
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

Record_time = datetime.datetime.strptime(lasttime,"%Y-%m-%d %H:%M:%S")
#------------------時間判斷式-------------------#

if datetime.datetime.now() < Record_time - datetime.timedelta(minutes=480) :
    print('ok')
else :
    print('在line上展示')
    message = "測試訊息。最後時間紀錄為 " +  str(lasttime)
    lineNotifyMessage(token, message)


#------------------測試訊息-------------------#
#message = "測試訊息。"
#lineNotifyMessage(token, message)


endtime = datetime.datetime.now()  #計算結束時間
print (endtime - starttime)