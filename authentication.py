import json

class Auth:
    def __init__(self):
        self.users = None
            
    
    def read(self):
        with open('users.json', 'r', encoding='utf-8') as FileR:
            data = json.loads(FileR.read())
            FileR.close()
        return data
    
    
    def write(self, data):
        with open('users.json', 'w', encoding='utf-8') as FileW:
            FileW.write(json.dumps(data, indent=4, ensure_ascii=False))
            FileW.close()
    
    
    def load_users(self):
        try:
            data = self.read()
            self.users = data
            
        except:
            data = {
                'users': [
                    {
                        'id': 1234567890,
                        'name': 'exemple'
                    }
                ]
            }
            
            self.write(data=data)
            self.users = data
    
    
    def auth_by_id(self, id):
        for user in self.users['users']:
            if user['id'] == id:
                return True
    
    
    def add_user(self, name, id):
        data = self.read()
        if {'id': id, 'name': name} not in data['users']:
            data['users'].append({'id': id, 'name': name})
            self.write(data=data)
            self.load_users()
            return True