from dotenv import load_dotenv
import os
import json

load_dotenv()

MOD_PATH = os.getenv("MOD_PATH")
MODLIST_PATH = os.getenv("MODLIST_PATH")
LOG_PATH = "debug.log"
MOD_JSON = "mod_dict.json"

def log_debug(msg: str) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as dbug:
        dbug.write(msg + "\n")


def data_import():

    # clear debug log
    open(LOG_PATH, "w").close()

    #open and capture modlist.txt
    with open(f'{MODLIST_PATH}', 'r', encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')

    # List for all mods in modlist.txt
    mods = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('+'):     # active mods are prefixed with a '+', disabled mods and separators are listed with '-'
            mods.append(line[1:])

    # sorted list of mods for ease of search in json
    mods.sort()

    # mods with no ini files are captured - Not currently handled further
    no_ini = []

    # final dictionary to be exported as JSON
    mods_dict = {}

    for mod in mods:

        try:
            with open(f'{MOD_PATH}{mod}/meta.ini', 'r', encoding="utf-8") as ini:
                ini_content = ini.read()

        # to catch and pass over mods with no ini files
        except FileNotFoundError:
            log_debug(f'DEBUGGER:  INFO:     {mod} has no meta.ini file')
            no_ini.append(mod)
            continue

        log_debug(f'DEBUGGER - INFO:     {mod} has meta.ini file')

        ini_line = ini_content.split('\n')

        # dict for each mod in mods_dict
        append_dict = {}

        for line in ini_line:
            if line.startswith('['):   # category line to be ignored
                log_debug(f'DEBUGGER - INFO:     passed line:       {line}')
                continue

            # specific handling of nexus description, as it is a minefield of chars and needs to be inserted manually - consider split('=', 1) to handle
            elif line.startswith('nexusDescription'):
                key = 'nexusDescription'
                value = line[(len('nexusDescription')+2)::]
                append_dict[key] = value
                log_debug(f'DEBUGGER - INFO:     forced insertion:  {key}: {value}:  ')
                continue

            else:
                try:
                    (key, val) = line.split('=')
                    log_debug(f'DEBUGGER - INFO:     successful split:  {key} = {val}')
                    append_dict[key] = val
                except ValueError as err:
                    # currently im only seeing empty lines show up. I could handle them, but I want to see if anything new happens in the future
                    log_debug(f'DEBUGGER - WARNING:  {err}:  skipped value:\n{line}')
                    # append_dict[key] = ''
                    pass

        mods_dict[mod] = append_dict

    with open(f'{MOD_JSON}', 'w', encoding="utf-8") as mod_export:
        json.dump(mods_dict, mod_export, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    data_import()