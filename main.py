import os
import json
import typer
from save_editor import SaveEditor


app = typer.Typer()

@app.command()
def parse(game:str, platform:str, version:str, filepath:str, output:str=""):
    se = SaveEditor(game, platform, version)
    with open(filepath, 'rb') as f:
        data_dict = se.parse(f.read())

    output = output if output else os.path.basename(filepath)
    output += ".json"
    with open(output, 'w') as f:
        json.dump(data_dict, f, indent=4)
        print("Success! File parsed and saved to: ", output)

@app.command()
def edit(game:str, platform:str, version:str, filepath:str, jsonpath:str, output:str=""):
    se = SaveEditor(game, platform, version)
    with open(filepath, 'rb') as f:
        save_bytes =f.read()
    
    with open(jsonpath, 'r') as f:
        save_data = json.load(f)
    
    edited_bytes = se.edit(save_data, save_bytes)

    output = output if output else os.path.basename(filepath)
    output += ".edited"
    with open(output, 'wb') as f:
        f.write(edited_bytes)
        print("Success! File edited and saved to: ", output)

@app.command()
def convert(game:str, platform:str, version:str, filepath:str):
    print("Sorry Not yet supported.")

if __name__ == "__main__":
    app()