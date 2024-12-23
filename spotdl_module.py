import os
import json
from utils import panic, run_command

query = os.environ["QUERY"]
codec = os.environ["CODEC"]

command = [
    'spotdl'
]

with open("configs/spotdl.json") as config:
    for key, values in json.load(config).items():
        if key != 'format' or codec == 'ORIGINAL':
            command.append(f"--{key}")
            if type(values) is str:
                command.append(values)
            elif type(values) is list:
                for i in values:
                    command.append(i)
            else:
                command.append(str(values))

if codec != 'ORIGINAL':
    command.append('--format')
    command.append(codec.lower())

command.append('download')

command.append(query.strip())

print(f"[INFO] {query}, codec: {codec}")

print(command)
run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")