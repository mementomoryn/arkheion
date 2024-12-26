import os
from utils import panic, run_command

select = os.environ["COMMANDS"]
query = os.environ["QUERY"]
quality = os.environ["QUALITY"]

config_file = "'modules/tidal-dl-ng/config.json'"
if os.path.isfile(config_file) == True:
  run_command(["mv", config_file, "'$HOME/.config/tidal_dl_ng/settings.json'"])

if quality != "":
    run_command(["tdn", "cfg", "quality_audio", quality.replace(" ", "_")])

def cli_commands(select):
    match (select):
        case "DOWNLOAD":
            return "dl"
        case "LOGIN":
            return "login"
        case _
            panic("[ERROR] Unrecognizable commands")

command = [
    'tdn'
]

command.append(map(cli_commands, select))

if select == "DOWNLOAD":
  command.append(query.strip())

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
