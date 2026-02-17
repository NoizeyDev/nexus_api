from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

import requests, json

ENDPOINT = "https://api.nexusmods.com/v2/graphql"

query = """
query fileHash($md5: String!) {
  fileHash(md5: $md5) {
    createdAt
    fileName
    fileSize
    fileType
    gameId
    md5
    modFile {
      fileId,
      name,
      totalDownloads
    }
    modFileId
  }
}
"""

variables = {
    "md5": "60385f7094908527b0823a0497b764b6"
}

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY
}

resp = requests.post(
    ENDPOINT,
    json={"query": query, "variables": variables},
    headers=headers,
)

resp.raise_for_status()
data = resp.json()
print(json.dumps(data, indent=2))