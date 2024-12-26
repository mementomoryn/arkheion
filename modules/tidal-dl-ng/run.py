import os
from utils import panic, run_command

select = os.environ["COMMANDS"]
query = os.environ["QUERY"]

def cli_commands(select):
    match (select):
        case "DOWNLOAD":
            return "dl"
        case "LOGIN":
            return "login"

command = [
    'tdn'
]

command.append(map(cli_commands, select))

if select == "DOWNLOAD"
  command.append(query.strip())

run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
