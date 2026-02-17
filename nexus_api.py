from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

import requests
class NexusModsAPI:

    def __init__(self, game='skyrimspecialedition'):
        self.game = game
        self.mod_id = 171835
        self.period = '1d'
        self.mod_version_id = ''
        self.md5_hash = '60385f7094908527b0823a0497b764b6'
        self.file_id = 661259
        self.game_id = 1704

    #***********    MODS   *************

    #GET /v1/games/{game_domain_name}/mods/updated.json
    def get_mod_updated(self):
        """
        Nexus API Get Request\n
        :return JSON, a list of mods that have been updated in a given period\n
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/updated.json?period={self.period}'
        _headers = {'apikey': API_KEY, 'accept': 'application/json'}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #GET /v1/games/{game_domain_name}/mods/{mod_id}/changelogs.json
    def get_mod_changelogs(self):
        """
        Nexus API Get Request\n
        :return: JSON, Changelogs for modID
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/{self.mod_id}/changelogs.json'
        _headers = {'apikey': API_KEY, 'accept': 'application/json'}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    # GET /v1/games/{game_domain_name}/mods/latest_added.json
    def get_mod_latest_added(self):
        """
        Nexus API Get Request\n
        Retrieve 10 latest added mods for a specified game\n
        :return: JSON
        """

        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/latest_added.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    # /v1/games/{game_domain_name}/mods/latest_updated.json
    def get_mod_latest_updated(self):
        """
        Nexus API Get Request\n
        Retrieve 10 latest updated mods for a specified game\n
        :return: JSON
        """

        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/latest_updated.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    # /v1/games/{game_domain_name}/mods/trending.json
    def get_mod_latest_trending(self):
        """
        Nexus API Get Request\n
        Retrieve 10 latest trending mods for a specified game\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/trending.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #GET /v1/games/{game_domain_name}/mods/{id}.json
    def get_mod(self):
        """
        Nexus API Get Request\n
        Retrieve specified mod, from a specified game. Cached for 5 minutes.
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/{self.mod_id}.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #GET /v1/games/{game_domain_name}/mods/md5_search/{md5_hash}.json
    def get_mod_md5(self):
        """
        Nexus API Get Request\n
        Looks up a file MD5 file hash
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/md5_search/{self.md5_hash}.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #POST /v1/games/{game_domain_name}/mods/{id}/endorse.json
    def post_mod_endorse(self):
        """
        Nexus API Post Request\n
        User-> Endorse Mod\n
        :return: Success or failure message:
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/{self.mod_id}/endorse.json'
        _headers = {'apikey': API_KEY, 'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' }
        _data = {"version": f'{self.mod_version_id}'} #4.3.6c
        return requests.post(url, headers=_headers).json()

    #POST /v1/games/{game_domain_name}/mods/{id}/abstain.json
    def post_mod_abstain_endorse(self):
        """
        Nexus API Post Request\n
        User-> Abstain from Endorse Mod\n
        :return: Success or failure message:
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/{self.mod_id}/abstain.json'
        _headers = {'apikey': API_KEY, 'Content-Type': 'application/x-www-form-urlencoded' }
        _data = {"version": f'{self.mod_version_id}'} #4.3.6c
        return requests.post(url, headers=_headers).json()

    # ***********    MOD Files   *************

    #GET /v1/games/{game_domain_name}/mods/{mod_id}/files.json
    def get_mod_files(self):
        """
        Nexus API Get Request\n
        Lists all files for a specific mod\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/{self.mod_id}/files.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #/v1/games/{game_domain_name}/mods/{mod_id}/files/{file_id}.json
    def get_mod_specific_file(self):
        """
        Nexus API Get Request\n
        View a specified mod file\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/{self.mod_id}/files/{self.file_id}.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #/v1/games/{game_domain_name}/mods/{mod_id}/files/{id}/download_link.json
    def get_mod_download_link(self):
        """
        Nexus API Get Request\n
        View a specified mod file\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}/mods/{self.mod_id}/files/{self.file_id}/download_link.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    # ***********    Games   *************

    #/v1/games.json
    def get_all_games(self):
        """
        Nexus API Get Request\n
        Returns a list of all games\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #/v1/games/{game_domain_name}.json
    def get_game(self):
        """
        Nexus API Get Request\n
        Returns information about a game\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/games/{self.game}.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()


    # ***********    User   *************

    #/v1/users/validate.json
    def get_validate_api(self):
        """
        Nexus API Get Request\n
        Returns to validate API key\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/users/validate.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    #/v1/user/tracked_mods.json
    def get_tracked_mods(self):
        """
        Nexus API Get Request\n
        Returns a list of all tracked mods\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/user/tracked_mods.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()


    #POST /v1/user/tracked_mods.json
    def post_mod_track(self):
        """
        Nexus API Post Request\n
        User-> Track Mod\n
        :return: Success or failure message:
        """
        url = f'https://api.nexusmods.com/v1/user/tracked_mods.json?domain_name={self.game}'
        _headers = {'apikey': API_KEY, 'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' }
        _data = {"mod_id": {self.mod_id}}
        _response = requests.post(url, headers=_headers, data=_data)
        return _response.json()

    #DELETE /v1/user/tracked_mods.json
    def delete_tracked_mods(self):
        """
        Nexus API DELETE Request\n
        Request to stop tracking a mod\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/user/tracked_mods.json?domain_name={self.game}'
        _headers = {'apikey': API_KEY, 'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' }
        _data = {"mod_id": self.mod_id}
        _response = requests.delete(url, headers=_headers, data=_data)
        return _response.json()

    #GET /v1/user/endorsements.json
    def get_all_endorsements(self):
        """
        Nexus API Get Request\n
        Returns a list of all endorsements\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/user/endorsements.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()

    # ***********    User   *************

    # /v1/colourschemes.json
    def get_colour_schemes(self):
        """
        Nexus API Get Request\n
        Returns list of all colour schemes\n
        :return: JSON
        """
        url = f'https://api.nexusmods.com/v1/colourschemes.json'
        _headers = {'apikey': API_KEY}
        _response = requests.get(url, headers=_headers)
        return _response.json()
