from google.cloud import vision
import uuid
import time
import json
import os
import io

class ComputerVision:
    def __init__(self, config):
        self.config = config
        
        
    def get_file_path(self):
        uuid_v4 = uuid.uuid4()
        
        file_path = os.path.join(self.config['folder_name'], f'{uuid_v4}.{self.config['format_img']}')
        os.makedirs(self.config['folder_name'], exist_ok=True)
        return file_path
    

    def extract_text(self, file_path):
        try:
            client = vision.ImageAnnotatorClient.from_service_account_file(self.config['google_key_path'])
            
            with io.open(file_path, 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)
            
            response = client.text_detection(image=image)
            texts = response.text_annotations
            
            if texts:
                list_texts = texts[0].description.split('\n')
                print('='*100, '\nGoogle Cloud Vision:\n'+json.dumps(list_texts, indent=4, ensure_ascii=False)+'\n')
                return list_texts
            else:
                print('Google Cloud Vision: Nenhum texto detectado!')

            if response.error.message:
                raise Exception(f'Erro: {response.error.message}')
        
        except Exception as e:
            print(f'Erro {e} em Google Cloud Vision API. Tentando Novamente..')
            time.sleep(1)
            return self.extract_text(file_path)