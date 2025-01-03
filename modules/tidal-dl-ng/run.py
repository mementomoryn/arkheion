import os
import subprocess
from modules.utils import panic, run_command

select = os.environ["COMMAND"]
query = os.environ["QUERY"]
quality = os.environ["QUALITY"]

config_file = "'modules/tidal-dl-ng/config.json'"
print("Moving configured config.json...")
if os.path.isfile(config_file) == True:
  run_command(["mv", "-f", config_file, "'home/runner/.config/tidal_dl_ng/settings.json'"])

token_file = "'modules/tidal-dl-ng/token.json'"
print("Moving user configured token.json...")
if os.path.isfile(token_file) == True:
  run_command(["mv", "-f", token_file, "'home/runner/.config/tidal_dl_ng/token.json'"])

if quality != "AUTO":
    run_command(["tidal-dl-ng", "cfg", "quality_audio", quality.replace(" ", "_")])

def cli_commands(select):
    match (select):
        case "DOWNLOAD":
            return "dl"
        case "LOGIN":
            return "login"
        case _:
            panic("[ERROR] Unrecognizable commands")

command = [
    'tidal-dl-ng'
]

command.append(cli_commands(select))

if select == "DOWNLOAD":
  command.append(query.strip())

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
