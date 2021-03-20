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


def read_values(letter):
    range_names = []
    range_names.append(letter+'8')
    range_names.append(letter+'11')
    range_names.append(letter+'12')
    result = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id, ranges=range_names).execute()
    ranges = result.get('valueRanges', [])
    # print('{0} ranges retrieved.'.format(len(ranges)))
    return ranges


def write_values(range_name):
    pass
