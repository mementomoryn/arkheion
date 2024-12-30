import os
from modules.utils import panic, run_command

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

command.append(' '.join('"' + query_untracked_list.strip() + '"'))

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
