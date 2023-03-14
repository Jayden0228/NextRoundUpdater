from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '17NmPOmL6Mzu2jYSmDxu5pWhlAnzaPkB5je7OKr8atVo'

try:
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="R1!A1:A").execute()

    values = result.get('values', [])
    print(values)

except HttpError as err:
    print(err)


r2=[["Jyden"]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="R2!A1", valueInputOption="USER_ENTERED", body={"values":r2}).execute()