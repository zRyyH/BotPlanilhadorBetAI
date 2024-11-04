import json


class Models:
    def __init__(self):
        self.models = None
    
    def read(self):
        with open('models.json', 'r', encoding='utf-8') as FileR:
            data = json.loads(FileR.read())
            FileR.close()
        return data
    
    
    def write(self, data):
        with open('models.json', 'w', encoding='utf-8') as FileW:
            FileW.write(json.dumps(data, indent=4, ensure_ascii=False))
            FileW.close()
            

    def load_models(self):
        try:
            data = self.read()
            self.models = data['models']
            
        except:
            data = {
                "models": [
                    {
                        "input": 
                            [
                                "R$750,00 Simples", 
                                "• CRIAR APOSTA PERSONALIZADA 1.83", 
                                "Man Utd", 
                                "FC Twente", 
                                "Bruno Fernandes - Mais de 0.5 Faltas Cometidas", 
                                "Jogador - Faltas Cometidas - Mais Alternativas", 
                                "Ricky van Wolfswinkel - Mais de 0.5 Faltas Cometidas", 
                                "Jogador - Faltas Cometidas - Mais Alternativas", 
                                "Se o jogador não começar, as seleções que referem-se a ele serão anuladas.", 
                                "As odds serão recalculadas para as seleções restantes.", 
                                "Qua 25 Sep", 
                                "16:00", 
                                "Aposta", 
                                "R$750,00", 
                                "Retornos", 
                                "R$1.375,00", 
                                "Encerrar Aposta R$625,00"
                                ],
                        "output":
                            {
                                "Aposta": "750,00",
                                "Odd": "1.50",
                                "Fixture": "Man Utd vs Tottenham",
                                "Bet": "Bruno Fernandes - Mais de 0.5 Faltas Cometidas + Ricky van Wolfswinkel - Mais de 0.5 Faltas Cometidas",
                                "Tipo": "Criar Aposta Personalizada",
                                "Data": "25/09",
                                "Hora": "16:00"
                                }
                    },
                    {
                        "input": 
                            [
                                "R$1.125,00 Simples",
                                "• Slavia Praga +0.5 1.950",
                                "Handicap Asiático - Cartões",
                                "Slavia Praga",
                                "Ajax",
                                "Aposta",
                                "R$1125,00",
                                "Retornos",
                                "R$2.193,75",
                                "Encerrar Aposta R$975,00",
                                "Editar"
                                ],
                        "output":
                            {
                                "Aposta": "1125,00",
                                "Odd": "1.95",
                                "Fixture": "Slavia Praga vs Ajax",
                                "Bet": "Slavia Praga +0.5",
                                "Tipo": "Handicap Asiático - Cartões",
                                "Data": "XX/XX",
                                "Hora": "XX:XX"
                                }
                    },
                    {
                        "input": 
                            [
                                "R$400,00 Simples", 
                                "° Menos de 83.5 1.83", 
                                "1º Tempo - Totais", 
                                "Cojute", 
                                "Brujos Izalco", 
                                "Aposta", 
                                "R$400,00", 
                                "Editar", 
                                "Encerrar Aposta R$400,00", 
                                "Sex 27 Sep", 
                                "22:15", 
                                "Retornos", 
                                "R$733,33"
                                ],
                        "output":
                            {
                                "Aposta": "400,00",
                                "Odd": "1.25",
                                "Fixture": "Cojute vs Brujos Izalco",
                                "Bet": "Menos de 83.5",
                                "Tipo": "1º Tempo - Totais",
                                "Data": "27/09",
                                "Hora": "22:15"
                                }
                    }
                ]
            }
            
            self.write(data=data)
            self.models = data['models']
            
            
    def get_models(self):
        return self.models