import os
import sys

def panic(message: str):
    print(message, file=sys.stderr)
    exit(1)
                
def run_command(command: list):
    print("[INFO]" + " ".join(command))
    os.system(" ".join(command))
    
def map_splice(str):
    return '"' + str.strip() + '"'

def set_github_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)
