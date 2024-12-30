import os
from modules.utils import panic, map_splice, run_command

query = os.environ["QUERY"]
query_untracked = query.split("si=")[0]
quality = os.environ["QUALITY"]

command = [
    'gytmdl'
    '--config-path',
    'modules/votify/config.toml'
]

if quality != 'AUTO':
    command.append('--itag')
    command.append(int(quality))

query_untracked_list = query_untracked.split('&&')

command.append(' '.join(map(map_splice, query_untracked_list)))

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")