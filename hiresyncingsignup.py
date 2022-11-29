import json

import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

# API URL
url1 = "http://ec2-3-17-167-77.us-east-2.compute.amazonaws.com:8000/api/v1/users"
# Sign UP
file1 = open("C:\\Users\\athir\\\PycharmProjects\\ROH_APIs\\userdetails.json", 'r')
json_input = file1.read()
request_json = json.loads(json_input)

# Post request with json input body
response = requests.post(url1, json=request_json)
hirestatus = response.status_code

print(hirestatus)
print("STATUS", hirestatus)

#GET user id from API response
print(response.json())
resp = response.json()
uid = resp['data']['user_id']
token = resp['data']['temp_token']
print(uid)
print(token)
print(resp.keys())

# Updates Data in to the sheet
scopes = [
     'https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("../secretkeys.json", scopes=scopes)

# Open sheet
file = gspread.authorize(creds)
workbook = file.open("userid")
sheet = workbook.sheet1
sheet.update_cell(2, 1, uid)



