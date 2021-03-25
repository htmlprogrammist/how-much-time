import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import tokens

CREDENTIALS_FILE = 'credentials.json'
spreadsheet_id = tokens.spreadsheet_id
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def read_values(letter, even):
    range_names = []  # ['B8', 'B11', 'B12']
    if not even:
        range_names.append(letter + '8')
    else:
        range_names.append(letter + '11')
        range_names.append(letter + '12')
    print(range_names)  # Он тупо чередует их поперекрёстно. B8, потом не B11 и B12
    # ... а C11, C12
    result = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id, ranges=range_names).execute()
    return result.get('valueRanges', [])


def write_values(value, position):
    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "{0}".format(position),
                 "majorDimension": "ROWS",
                 "values": [[value]]},
            ]
        }
    ).execute()
