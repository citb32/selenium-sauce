#!/bin/python 

import requests
import json
import sys
IP=sys.argv[1]

listurl = "http://"+IP+"/student/student/list"
posturl = "http://"+IP+"/student/student"


#### LIST
headers = {}
response = requests.request("GET", listurl, headers=headers)
jsonout = json.loads(response.text)
if jsonout['httpStatus'] >=400:
    print "API TEST - LIST -  FAILURE"
else:
    print "API TEST - LIST - SUCCESS"


#### POST
payload = "{\r\n\t  \"studentName\": \"Meghan Mahadev\",\r\n      \"studentAddr\": \"Hyderabad\",\r\n      \"studentAge\": \"2\",\r\n      \"studentQulaification\": \"Nursary\",\r\n      \"studentPercent\": \"99%\",\r\n      \"studentYearPassword\": \"2017\"\r\n}"
headers = {
    'content-type': "application/json",
    }
response = requests.request("POST", posturl, data=payload, headers=headers)
jsonout = json.loads(response.text)
if jsonout['httpStatus'] >=400:
    print "API TEST - POST -  FAILURE"
else:
    print "API TEST - POST - SUCCESS"
ID=jsonout['data']['object']['student_id']

#### DELETE
delurl = "http://"+IP+"/student/student/"+str(ID)
headers = {}
response = requests.request("DELETE", delurl, headers=headers)
jsonout = json.loads(response.text)
if jsonout['httpStatus'] >=400:
    print "API TEST - DELETE -  FAILURE"
else:
    print "API TEST - DELETE - SUCCESS"
