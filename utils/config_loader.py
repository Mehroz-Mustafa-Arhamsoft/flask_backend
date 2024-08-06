import json

class Configuration:
    def __init__(self, filename):
        self.filename = filename
        self.load_config()
    
    def load_config(self):
        with open(self.filename, 'r') as f:
            content = f.read()
            self.config_data = json.loads(content)

    def get_tools(self):
        return self.config_data["tools"]