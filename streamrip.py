import os
from utils import run_command

options = os.getenv['COMMANDS']

streamrip = [
    'python',
    '-m',
    'rip',
    options
]

match options:
    case 'id':
        streamrip.append(os.getenv['TRACK_ID'])
    case 'url':
        streamrip.append(os.getenv['TRACK_URL'])
    case 'search':
        streamrip.append(os.getenv['SOURCES'])
        streamrip.append(os.getenv['TYPES'])
        streamrip.append(os.getenv['QUERY'])
    case 'lastfm':
        streamrip.append(os.getenv['LASTFM_URL'])

if options != 'search':
    quality = os.getenv['QUALITY']
    if quality == 'default':
        streamrip.append(quality)
        
    codec = os.getenv['CODEC']
    if codec == 'original':
        streamrip.append(codec)
        
    run_command(streamrip, 'print')
else:
    output = run_command(streamrip, 'return', 60)
