import os
import datetime
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from data_parse import summa
from dotenv import load_dotenv
load_dotenv()

scope = [os.getenv('scope_one'), os.getenv('scope_two')]
creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('json_keyfile'), scope)
client = gspread.authorize(creds)
sheet = client.open(os.getenv('name_sheet')).sheet1

# test = sheet.get_all_records()
# print(test)

def getyesterday():
    today = datetime.now()
    yesterday = today + timedelta(days=-1)
    if yesterday.day < 10:
        day = '0' + str(yesterday.day)
    else:
        day = str(yesterday.day)
    if yesterday.month < 10:
        month = '0' + str(yesterday.month)
    else:
        month = str(yesterday.month)
    yesterday_correct = day + '.' + month + '.' + str(yesterday.year)
    return yesterday_correct
    # str_yesterday = str(yesterday.day) + '.' + str(yesterday.month) + '.' + str(yesterday.year)


search = sheet.find(getyesterday())
row_col = sheet.update_cell(int(search.row), int(search.col) + 2, str(summa))
