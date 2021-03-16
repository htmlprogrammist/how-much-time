import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import tokens

CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = tokens.spreadsheet_id
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
stdin = input()


def main(value):
    start_time_hours = int(value.split(' - ')[0].split(':')[0])  # получаю значение часа
    start_time_minutes = int(value.split(' - ')[0].split(':')[1])  # получаю значение минут
    end_time_hours = int(value.split(' - ')[1].split(':')[0])  # Аналогично
    end_time_minutes = int(value.split(' - ')[1].split(':')[1])  # Аналогично
    # 8:15 - 10:05 => '8:15', '10:05' => 8, 15, 10, 5
    diff_hours = end_time_hours - start_time_hours
    diff_minutes = end_time_minutes - start_time_minutes
    if diff_minutes < 0:
        diff_hours -= 1
        diff_minutes = 60 + diff_minutes  # 60 + (-10) = 50
    while diff_hours > 0:
        diff_minutes += 60
        diff_hours -= 1
    amount_of_hours = round(diff_minutes / 60, 2)
    print(amount_of_hours)


main(stdin)
