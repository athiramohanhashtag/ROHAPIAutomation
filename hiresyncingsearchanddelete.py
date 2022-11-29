import json
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
     'https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("../secretkeys.json", scopes=scopes)

# Open sheet
file = gspread.authorize(creds)
workbook = file.open("userid")
sheet = workbook.sheet1
uid = int(sheet.acell('A2').value)
print(uid)


# API URL
api_name = "Hire Search"
url = "http://ec2-3-144-164-248.us-east-2.compute.amazonaws.com:8001/api/users"

# Read input JSON file
file1 = open('C:\\Users\\athir\\PycharmProjects\\ROH_APIs\\hirecordinates.json', 'r')
json_input = file1.read()
request_json = json.loads(json_input)

# Make POST request with Json input body
response = requests.post(url, json=request_json)
values = response.json()
hirestatus = response.status_code

print("STATUS", hirestatus)
print(values)
all_ids = []
#Store user ids into list
for value in values:
    all_ids.append(value['user_id'])

print(all_ids)
#Comparison
#print(type(uid))
if uid in all_ids:

    print("User exists")
else:
    print("User not in the list")

