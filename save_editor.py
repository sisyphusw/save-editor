import importlib
import json

class SaveEditor():

    def __init__(self, game_name:str, platform:str, version:str):
        format_str = lambda s: s.strip().lower().replace(' ', '_').replace('.', '_')

        self.name = format_str(game_name)
        self.platform = format_str(platform)
        self.version = format_str(version)
        
        self.module = importlib.import_module(f'{self.name}.{self.platform}.{self.version}')

    def parse(self, save_bytes:bytes) -> dict:
        return self.module.parse(save_bytes)
    
    def edit(self, save_data:dict, save_bytes:bytes) -> bytes:
        return self.module.edit(save_data, save_bytes)

    # Todo
    def convert(self, to_platform:str, save_bytes:bytes) -> bytes:
        pass

# for test
if __name__ == "__main__":
    save_path = 'example/UCSAVEFILE03.DAT'
    save_bytes = open(save_path, 'rb').read()
    se = SaveEditor('Unicorn Overlord', 'Switch', 'v1.00')
    save_data = se.parse(save_bytes)
    json.dump(save_data, open('output1.json', 'w'))
    pass