import os
from modules.utils import panic, run_command

query = os.environ["QUERY"]
query_untracked = query.split("si=")[0]
codec = os.environ["CODEC"]
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

output_path = r"'music/{artist}/{album} ({year})/{artist} - {title}.{output-ext}'"

audio_providers = [
    "youtube-music",
    "bandcamp",
    "soundcloud",
    "youtube"
]

lyrics_providers = [
    "musixmatch",
    "synced",
    "genius",
    "azlyrics"
]

command = [
    'spotdl',
    '--client-id',
    client_id,
    '--client-secret',
    client_secret,
    '--audio',
    " ".join(audio_providers),
    '--lyrics',
    " ".join(lyrics_providers),
    '--sponsor-block',
    '--no-cache',
    '--preload',
    '--dont-filter-results',
    '--generate-lrc',
    '--print-errors',
    '--log-level',
    'INFO',
     '--cookie-file',
     'cookies.txt'
]

command.append('--format')
if codec != 'ORIGINAL':
    command.append(codec.lower())
else:
    command.append('opus')

command.append('download')

query_untracked_list = query_untracked.split('&&')

command.append(' '.join('"' + map(str.strip, query_untracked_list) + '"'))

command.append('--output')
command.append(output_path)

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
