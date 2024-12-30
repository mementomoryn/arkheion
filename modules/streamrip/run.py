import os
from modules.utils import panic, run_command

select = os.environ["COMMAND"]
service = os.environ["SERVICE"]
type = os.environ["TYPE"]
query = os.environ["QUERY"]
quality = os.environ["QUALITY"]
codec = os.environ["CODEC"]

query_list = query.split('&&')

for query in query_list:
    command = [
        'rip',
        '--config-path',
        'modules/streamrip/config.toml'
    ]

    if select != 'CONFIG RESET':
        if quality != 'AUTO':
            command.append('--quality')
            command.append(int(quality))
                
        # if codec != 'ORIGINAL':
        #     command.append('--codec')
        #     command.append(codec.lower())

        command.append(select.lower())

        if select == 'SEARCH':
            command.append('--first')
            command.append(service.lower())
            command.append(type.lower())

        command.append('"' + query.strip() + '"')

    run_command(command)

# if os.path.exists("music") is False:
    # panic("[ERROR] Downloads folder does not exist")
