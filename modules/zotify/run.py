import os
from modules.utils import panic, map_splice, run_command

query = os.environ["QUERY"]
query_untracked = query.split("?si=")[0]
format = os.environ["FORMAT"]
quality = os.environ["QUALITY"]

command = [
    'zotify',
    '--credentials-location="credentials.json"',
    '--root-path="music"',
    '--root-podcast-path="music"',
    r'--output="{artist}/{album} ({release_year})/{artist} - {song_name}.{ext}"',
    '--skip-existing=False',
    '--print-downloads=True',
    '--bulk-wait-time=5'
    
]

if format != 'AUTO':
    format_command = format.lower().replace(" ", "_")
else:
    format_command = 'aac'
command.append(f'--download-format={format_command}')
    
if quality != 'AUTO':
    quality_command = quality.lower().replace(" ", "_")
else:
    quality_command = 'high'
command.append(f'--download-quality={quality_command}')

query_untracked_list = query_untracked.split('&&')

command.append(' '.join(map(map_splice, query_untracked_list)))

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
