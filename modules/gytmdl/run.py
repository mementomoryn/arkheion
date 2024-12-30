import os
from modules.utils import panic, run_command

query = os.environ["QUERY"]
query_untracked = query.split("si=")[0]
itag = os.environ["ITAG"]

command = [
    'gytmdl'
    '--config-path',
    'modules/gytmdl/config.toml'
]

if itag != 'AUTO':
    command.append('--itag')
    command.append(int(itag))

query_untracked_list = query_untracked.split('&&')

command.append(' '.join('"' + map(str.strip, query_untracked_list) + '"'))

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
