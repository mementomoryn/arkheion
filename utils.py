import os
import requests
import subprocess
import sys

def panic(message: str):
    print(message, file=sys.stderr)
    exit(1)
    
def download(link, out, headers=None):
    if os.path.exists(out):
        print(f"{out} already exists skipping download")
        return

    with requests.get(link, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(out, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                
def run_command(command: list[str]):
    os.system(" ".join(command))

def set_github_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)