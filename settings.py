import json

class Settings:
    def __init__(self):
        self.config = None
            
    def read(self):
        with open('config.json', 'r', encoding='utf-8') as FileR:
            data = json.loads(FileR.read())
            FileR.close()
        return data
    
    def write(self, data):
        with open('config.json', 'w', encoding='utf-8') as FileW:
            FileW.write(json.dumps(data, indent=4, ensure_ascii=False))
            FileW.close()
            
    def load_settings(self):
        try:
            data = self.read()
            self.config = data
            
        except:
            data = {
                'password': '0000',
                'gpt_model': 'gpt-4o-mini',
                'format_img': 'jpg',
                'folder_name': 'screenshots',
                'chatgpt_token': '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',
                'spreadsheet_id': '1eJ1qYheJXv7FyJ-mDOKPFCZLHfhau0B89xlVF_Z1zw4',
                'telegram_token': '7640939296:AAE7RPghfco-L5Hero83uX33nmu5XVr3p8I',
                'google_key_path': 'chave.json',
            }
            
            self.write(data=data)
            self.config = data
            
    def auth(self, input_pass):
        if input_pass == self.password:
            return True
        
    def get_config(self):
        return self.config