from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

import requests

ENDPOINT = "https://api.nexusmods.com/v2/graphql"

# query unreliable. no pattern of what is available. If no errors in return message, then mod not linked to gql
query = """
query ModWithRequirements($filter: ModsFilter!, $count: Int!) {
  mods(filter: $filter, count: $count) {
    nodes {
      modId
      name
      author
      gameId
      summary
      uid
      viewerDownloaded
      modRequirements {
        nexusRequirements {
          nodes {
            externalRequirement
            gameId
            id
            modId
            modName
            notes
            url
          }
        }
      }
    }
  }
}
"""

def get_mod_with_requirements(game_id: int, mod_id: int):
    # gameid_modid are required as dict {key="value" : value=value}
    variables = {
      "filter": {
        "gameId": [{ "value": str(game_id)}],
        "modId": [{ "value": str(mod_id)}]
      },
        "count": 1
    }
    headers = {
        "Content-Type": "application/json",
        "apikey": API_KEY
    }

    resp = requests.post(
        ENDPOINT,
        json={"query": query, "variables": variables},
        headers=headers,
    )
    resp.raise_for_status()
    data = resp.json()
    return data

#only for testing hardcoded
if __name__ == '__main__':
    get_mod_with_requirements(1704, 171835)
