import requests
import gspread
import json
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from pycoingecko import CoinGeckoAPI
import datetime
import time

SERVICE_ACCOUNT_FILE = '' # Enter your service account file, found by following the Google API steps
SCOPES = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '' # Enter your spreadsheet ID which is found within the URL of your sheet

service = build('sheets','v4',credentials=creds)

sheet = service.spreadsheets()

pageNumber = 1
emptyCell = 2

for x in range(30):
      cgRawData = CoinGeckoAPI().get_coins_markets('USD',per_page=300,page=pageNumber)
      cgResult = [[token['name'],token['symbol'],token['current_price'],token['market_cap'],token['fully_diluted_valuation'],token['circulating_supply'],token['max_supply'],token['total_supply'],token['total_volume']] for token in cgRawData]
      cgVariableNotUsed = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='CoinGeckoDump!A%d'% emptyCell, valueInputOption="USER_ENTERED", body={"values":cgResult}).execute()
      pageNumber = pageNumber + 1
      emptyCell = emptyCell + 250

