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