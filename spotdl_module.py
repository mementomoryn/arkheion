import os
from utils import panic, run_command

query = os.environ["QUERY"]
codec = os.environ["CODEC"]

command = [
    'spotdl'
]

run_command(['mkdir', 'spotdl'])
run_command(['ln', 'configs/spotdl.json', 'spotdl/config.json'])
command.append('--config')

command.append('--log-level')
command.append('DEBUG')

if codec != 'ORIGINAL':
    command.append('--format')
    command.append(codec.lower())

command.append('download')

command.append(query.strip())

print(f"[INFO] {query}, codec: {codec}")

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")