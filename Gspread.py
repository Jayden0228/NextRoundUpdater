from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# SAMPLE_SPREADSHEET_ID = '17NmPOmL6Mzu2jYSmDxu5pWhlAnzaPkB5je7OKr8atVo'

def read(id, rng):
    
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id, range=rng+"!A1:A").execute()

        values = result.get('values', [])
        # print(values)
        return values

    except HttpError as err:
        print(err)

    return values




def write(id,rng,value):
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        
        # r2=[["Jyden"]]
        request = sheet.values().update(spreadsheetId=id, range=rng+"!A1", valueInputOption="USER_ENTERED", body={"values":value}).execute()

    except HttpError as err:
        print(err)


