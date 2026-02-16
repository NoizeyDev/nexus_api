from dotenv import load_dotenv
import os
load_dotenv()
MOD_PATH = os.getenv("MOD_PATH")
MODLIST_PATH = os.getenv("MODLIST_PATH")

import json

with open(f'{MODLIST_PATH}', 'r') as f:
    content = f.read()

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
        print(err, f'{mod} has no meta.ini file')
        no_ini.append(mod)
        continue

    print(f'{mod} has meta.ini file')
    ini_line = ini_content.split('\n')
    print(ini_line)
    append_dict = {}
    for line in ini_line:
        if ini_line[0] == '[':
            pass
        else:
            key = None
            try:
                (key, val) = line.split('=')
                print(f'successful split:  {key} = {val}')
                append_dict[key] = val
            except ValueError as err:
                print(err, f'key has no value, appending with no value')
                append_dict[key] = ''
                pass

        mods_dict[mod] = append_dict
        # print(f'mods_dict = {mods_dict}')


print(json.dumps(mods_dict, indent=4))
# print(f'no_ini\'s: {no_ini}')
# ini_lines = ini_content.split('\n')
# for lines in ini_lines:
#     lines = lines.strip("\n")
