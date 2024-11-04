from googleapiclient.discovery import build
from google.oauth2 import service_account
import time


class SheetsAPI:
    def __init__(self, config):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = service_account.Credentials.from_service_account_file(config['google_key_path'], scopes=SCOPES)
        
        self.service = build('sheets', 'v4', credentials=creds)
        self.config = config


    def get_first_sheet_name(self):
        try:
            sheet_metadata = self.service.spreadsheets().get(spreadsheetId=self.config['spreadsheet_id']).execute()
            sheets = sheet_metadata.get('sheets', '')
            
            if sheets:
                first_sheet_name = sheets[0]['properties']['title']
                return first_sheet_name
            else:
                raise Exception("Nenhuma aba encontrada na planilha")
        
        except Exception as e:
            print(f'Erro {e} em Google Sheets API. Tentando Novamente..')
            return self.get_first_sheet_name()
        
        
    def adicionar_aposta(self, data):
        try:
            Aposta = ','.join(str(data['Aposta']).split('.'))
            Odd = ','.join(str(data['Odd']).split('.'))
            
            Data = data['Data']
            Hora = data['Hora']
            
            Bet = data['Bet'].title()
            Tipo = data['Tipo'].title()
            Fixture = data['Fixture'].title()
            
            first_sheet_name = self.get_first_sheet_name()
            
            range = f'{first_sheet_name}!A:G'
            
            novos_dados = [Hora, Data, Fixture, Tipo, Bet, Aposta, Odd]
            
            body = {
                'values': [novos_dados]
            }
            
            print(f'Google Sheets API:\n{novos_dados}\n')
            
            result = self.service.spreadsheets().values().append(
                spreadsheetId=self.config['spreadsheet_id'], range=range,
                valueInputOption='USER_ENTERED', insertDataOption='OVERWRITE', body=body).execute()
            
            return result
        
        except Exception as e:
            print(f'Erro {e} em Google Sheets API. Tentando Novamente..')
            time.sleep(1)
            return self.adicionar_aposta(data)