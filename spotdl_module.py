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
run_command(['mkdir', '.spotdl'])
run_command(['ln', '-s', 'configs/spotdl.json', '.spotdl/config.json'])

if codec != 'ORIGINAL':
    command.append('--format')
    command.append(codec.lower())

print(f"[INFO] {select}: ({query}), codec: {codec}")

run_command(command)

if os.path.exists("music") is False:
    panic("[ERROR] Downloads folder does not exist")