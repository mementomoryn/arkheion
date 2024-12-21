import os
from utils import run_command

select = os.environ["COMMANDS"]
query = os.environ["QUERY"]
quality = os.environ["QUALITY"]
codec = os.environ["CODEC"]

command = [
    'rip',
    '--config-path',
    'configs/streamrip.toml'
]

if select != 'CONFIG RESET':
    if quality != 'AUTO':
        command.append('--quality')
        command.append(int(quality))
            
    if codec != 'ORIGINAL':
        command.append('--codec')
        command.append(codec)

    command.append(select.lower())

    command.append(query)
    
    print(f"[INFO] Downloading tracks/albums from {select} ({query}):\nquality: {quality}\n codec: {codec}")
else:
    print("[INFO] Resetting `config.toml`...")

run_command(command)

if len(os.listdir("music")) == 0:
    print("[ERROR] Downloads folder is empty")
    exit(1)
