import json
from nexus_api import NexusModsAPI
from data_import import data_import

request = NexusModsAPI()

# data_import()

with open("mod_dict.json", 'r', encoding="utf-8") as mods:
    mods_dict = json.load(mods)

print(mods_dict['ADXP MCO 1.6.0.6 Bug Fixes'])
# specific_mod = mods_dict[mod]
# print(json.dumps(specific_mod, indent=4))
# print(mod_list)