import gspread
import requests
import json
from oauth2client.service_account import ServiceAccountCredentials
#Edit Profile

scopes = [
     'https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("../secretkeys.json", scopes=scopes)

# Open sheet
file = gspread.authorize(creds)
workbook = file.open("token")
sheet = workbook.sheet1
user_id = int(sheet.acell('A2').value)
user_token = sheet.acell('B2').value
print(user_token)
#API URL
api_name = "Edit Profile"
user_token = f"Token {user_token}" #append string
headers = {"Authorization": user_token}

#user id is provided as path variable so the base url is store in a separate variable and the user id should be concatenate with base url as a string format.
base_url = "http://ec2-3-17-167-77.us-east-2.compute.amazonaws.com:8000/api/v1/employees/"
url = base_url+str(user_id)


#Read input JSON file
file2 = open("C:\\Users\\athir\\PycharmProjects\\ROH_APIs\\userprofile.json", 'r')
json_input = file2.read()
request_json = json.loads(json_input)
response = requests.patch(url, headers=headers, json=request_json)
editprofilestatus = response.status_code

print(editprofilestatus)
print(response.headers)
print(response.content)
