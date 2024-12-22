import os
import sys

def panic(message: str):
    print(message, file=sys.stderr)
    exit(1)
                
def run_command(command: list[str]):
    os.system(" ".join(command))

def set_github_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)