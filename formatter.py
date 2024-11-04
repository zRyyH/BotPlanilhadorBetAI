import json


def format_reply(data):
    result = f'''
Google Sheets

Hora: {data['Hora']}
Data: {data['Data']}
Fixture: {data['Fixture']}
Tipo: {data['Tipo']}
Bet: {data['Bet']}
Stake: {data['Aposta']}
Odd: {data['Odd']}

📊 Dados Adicionados!'''

    return result


def format_model(data):
    input = data['input']
    output = data['output']
    
    input_text = 'ENTRADA:\n'+json.dumps(input, ensure_ascii=False, indent=4)+'\n\n'
    output_text = 'SAIDA:\n'+json.dumps(output, ensure_ascii=False, indent=4)+'\n'
    
    result = input_text+output_text
    return result