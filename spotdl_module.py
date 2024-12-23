import os
from utils import panic, run_command

select = os.environ["COMMANDS"]
query = os.environ["QUERY"]
codec = os.environ["CODEC"]

command = [
    'spotdl'
]

command.append(select.lower())

command.append(query.strip())

command.append('--config')
command.append('configs/spotdl.json')

if codec != 'ORIGINAL':
    command.append('--format')
    command.append(codec.lower())

print(f"[INFO] {select}: ({query}):\nquality: {quality}\n codec: {codec}")

run_command(command)

if os.path.exists("music") is False:
    panic("[ERROR] Downloads folder does not exist")