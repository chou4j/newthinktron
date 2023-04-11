# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:00:49 2022

@author: scchou
"""
import requests
import datetime

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



#------------------測試訊息-------------------#
message = "測試訊息"
lineNotifyMessage(token, message)




endtime = datetime.datetime.now()  #計算結束時間
print (endtime - starttime)