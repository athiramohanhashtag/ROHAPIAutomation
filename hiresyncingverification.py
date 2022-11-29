import json

import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

# API URL
verification_url = "http://ec2-3-17-167-77.us-east-2.compute.amazonaws.com:8000/api/v1/users"
# Sign UP
file1 = open("C:\\Users\\athir\\\PycharmProjects\\ROH_APIs\\verificationcode.json", 'r')
json_input = file1.read()
request_json = json.loads(json_input)

# Post request with json input body
response = requests.patch(verification_url, json=request_json)
hirestatus = response.status_code

print(hirestatus)
print(response.content)

print(response.json())
resp = response.json()
uid = resp['data']['user_id']
user_token = resp['data']['token']

# Updates Data in to the sheet
scopes = [
     'https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("../secretkeys.json", scopes=scopes)

# Open sheet
file = gspread.authorize(creds)
workbook = file.open("token")
sheet = workbook.sheet1
sheet.update_cell(2, 1, uid)
sheet.update_cell(2, 2, user_token)
