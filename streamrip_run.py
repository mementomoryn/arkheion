import os
import sys
import asyncio
from utils import run_command

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

select = os.environ["COMMANDS"]
query = os.environ["QUERY"]
quality = os.environ["QUALITY"]
codec = os.environ["CODEC"]

command = [
    'rip',
    '--config-path',
    'configs\\streamrip.toml'
]

if select != 'config reset':
    if quality != 'config':
        command.append('--quality')
        command.append(int(quality))
            
    if codec != 'original':
        command.append('--codec')
        command.append(codec)

    command.append(select)

    command.append(query)
    
    print(f"[INFO] Downloading tracks/albums {select}: {query}, quality: {quality}, codec: {codec}")

os.system(" ".join(command))
