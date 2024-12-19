import os
from utils import run_command

options = os.getenv['COMMANDS']
track_id = os.getenv['TRACK_ID']
track_url = os.getenv['TRACK_URL']
lastfm_url = os.getenv['LASTFM_URL']
quality = os.getenv['QUALITY']
codec = os.getenv['CODEC']

command = [
    'python',
    '-m',
    'rip',
    '--config-path',
    'configs/streamrip.toml',
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
    command.append(int(quality))
        
if codec != 'original':
    command.append(codec)
        
run_command(command, 'print')
