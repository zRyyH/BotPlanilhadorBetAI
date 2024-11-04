import openai
import json
import time

from formatter import format_model


class GPTFilter:
    def __init__(self, config, models):
        openai.api_key = config['chatgpt_token']
        self.config = config
        self.models = models
        
        
    def normalize(self, bet_data):
        try:
            models = ''
            
            for model in self.models:
                models += format_model(model)
                
            messages = [
                {
                    "role": "user",
                    "content": (
                        "Por favor gere um JSON exatamente com as mesmas chaves, substitua apenas os valores, vou fornecer exemplos das entradas de dados e da saida esperada use para treinar.\n"
                        f"{models}"
                        "Retorne apenas o JSON no formato correto. Pronto para json.loads()\n"
                        f"{', '.join(bet_data)}"
                    )
                }
            ]
            
            response = openai.ChatCompletion.create(
                model=self.config['gpt_model'],
                messages=messages
            )
            
            res = response['choices'][0]['message']['content']
            res = json.loads('\n'.join(res.split('\n')[1:-1]))
            
            print(f'Normalizado pelo ChatGPT:\n{json.dumps(res, indent=4, ensure_ascii=False)}\n')
            
            return res
        
        except Exception as e:
            print(f'Erro {e} em ChatGPT API. Tentando Novamente..')
            time.sleep(1)
            return self.normalize(bet_data)