import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import main
import tokens

CREDENTIALS_FILE = 'credentials.json'
spreadsheet_id = tokens.spreadsheet_id
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def read_values(range_name):
    # range_name = 'B8'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    print(rows)
    print('{0} rows retrieved.'.format(len(rows)))
