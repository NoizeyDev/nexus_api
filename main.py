import json
from nexus_api import NexusModsAPI
from graphql_requirements import get_mod_with_requirements
from data_import import data_import

request = NexusModsAPI()

# data_import()

with open("mod_dict.json", 'r', encoding="utf-8") as mods:
    mods_dict = json.load(mods)


def mod_object(mod_name, _modsdict):
    request.mod_id = _modsdict[mod_name]['modid']
    request.file_id = _modsdict[mod_name]['1\\fileid']
    request.mod_version_id = _modsdict[mod_name]['version']

    # print(json.dumps(request.get_mod_specific_file(), indent=4))
    # print(json.dumps(request.get_mod(), indent=4))
    # print(json.dumps(request.get_mod_changelogs(), indent=4))
    # print(json.dumps(request.post_mod_track(), indent=4))
    # print(json.dumps(request.post_mod_endorse(), indent=4))

    mod_id = request.mod_id
    game_id = request.game_id
    print(mod_id, game_id)
    resp = get_mod_with_requirements( game_id, mod_id )

    nodes = resp["data"]["mods"]["nodes"]
    if not nodes:
        print(f"No NexusMods entry for game_id={game_id}, mod_id={mod_id}")
    else:
        mod = nodes[0]
        print(mod["name"])

    return json.dumps(resp, indent=4)


print(mod_object('RaceMenu', mods_dict))
