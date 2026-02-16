from dotenv import load_dotenv
import os
load_dotenv()
MOD_PATH = os.getenv("MOD_PATH")
MODLIST_PATH = os.getenv("MODLIST_PATH")
LOG_PATH = "debug.log"
MOD_JSON = "mod_dict.json"

import json

with open(f'{MODLIST_PATH}', 'r') as f:
    content = f.read()

open(LOG_PATH, "w").close()

def log_debug(msg: str) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as dbug:
        dbug.write(msg + "\n")

mods = []
lines = content.split('\n')
for line in lines:
    line = line.strip("\n")
    if not line:
        continue
    if line.startswith('+'):
        mods.append(line[1::])

mods.sort()
test = mods[3]
no_ini = []
mods_dict = {}
for mod in mods:

    try:
        with open(f'{MOD_PATH}{mod}/meta.ini', 'r', encoding="utf-8") as ini:
            ini_content = ini.read()
    except FileNotFoundError as err:
        log_debug(f'DEBUGGER:  INFO:     {mod} has no meta.ini file')
        no_ini.append(mod)
        continue
    log_debug(f'DEBUGGER - INFO:     {mod} has meta.ini file')

    ini_line = ini_content.split('\n')
    append_dict = {}

    for line in ini_line:
        if line.startswith('['):
            log_debug(f'DEBUGGER - INFO:     passed line:       {line}')
            continue
        elif line.startswith('nexusDescription'):
            key = 'nexusDescription'
            value = line[(len('nexusDescription')+2)::]
            append_dict[key] = value
            log_debug(f'DEBUGGER - INFO:     forced insertion:  {key}: {value}:  ')
            continue
        else:
            key = None
            try:
                (key, val) = line.split('=')
                log_debug(f'DEBUGGER - INFO:     successful split:  {key} = {val}')
                append_dict[key] = val
            except ValueError as err:
                log_debug(f'DEBUGGER - WARNING:  {err}:  skipped value:\n{line}')
                append_dict[key] = ''
                pass

        mods_dict[mod] = append_dict


open(MOD_JSON, "w").close()

with open(f'{MOD_JSON}', 'w') as mod_export:
    json.dump(mods_dict, mod_export, indent=4)

