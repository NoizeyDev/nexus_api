import json
from nexus_api import NexusModsAPI
import data_import

request = NexusModsAPI()
# response = request.get_request_mod_id()
# json_str = json.dumps(response, indent=4)
# print(json_str)
# print(request.post_mod_id_track().json())
# print(json.dumps(request.get_mod_changelogs(), indent=4))
# print(json.dumps(request.get_mod_full(), indent=4))
# print(json.dumps(request.get_mod_updated(), indent=4))
# print(json.dumps(request.post_mod_endorse(), indent=4))
# print(json.dumps(request.get_mod_latest_added(), indent=4))
# print(json.dumps(request.get_mod_latest_updated(), indent=4))å
# print(json.dumps(request.get_mod_md5(), indent=4))
# print(json.dumps(request.post_mod_abstain_endorse(), indent=4))
# print(json.dumps(request.get_mod_specific_file(), indent=4))
# print(json.dumps(request.get_mod_download_link(), indent=4))
# print(json.dumps(request.get_mod_download_link(), indent=4))
# print(json.dumps(request.get_all_games(), indent=4))
# print(json.dumps(request.get_game(), indent=4))
# print(json.dumps(request.get_validate_api(), indent=4))
# print(json.dumps(request.get_tracked_mods(), indent=4))
# print(json.dumps(request.post_mod_track(), indent=4))
# print(json.dumps(request.delete_tracked_mods(), indent=4))
# print(json.dumps(request.get_all_endorsements(), indent=4))

data_import.data_import()

