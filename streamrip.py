import os
from utils import run_command

options = os.environ["COMMANDS"]
track_id = os.environ["TRACK_ID"]
track_url = os.environ["TRACK_URL"]
lastfm_url = os.environ["LASTFM_URL"]
quality = os.environ["QUALITY"]
codec = os.environ["CODEC"]

command = [
    'rip',
    '--config-path',
    'configs\streamrip.toml',
    options
]

match options:
    case 'id':
        command.append(track_id)
    case 'url':
        command.append(track_url)
    case 'lastfm':
        command.append(lastfm_url)

if quality != 'default':
    command.append('--quality')
    command.append(quality)
        
if codec != 'original':
    command.append('--codec')
    command.append(codec)

print(f"command: {command}")
        
run_command(command, True)
