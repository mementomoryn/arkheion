import os
from utils import panic, run_command

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
        command.append(codec.lower())

    command.append(select.lower())

    command.append(query.strip())
    
    print(f"[INFO] ({select}) {query.strip()}, quality: {quality}, codec: {codec}")
else:
    print("[INFO] Resetting `config.toml`...")

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
