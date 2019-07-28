import requests #dependency
import json

url = "https://discordapp.com/api/webhooks/<irl>"
data = {}
#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
#data["content"] = "message content"
#data["username"] = "custom username"

#leave this out if you dont want an embed
data["embeds"] = []
embed = {}  
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
embed["description"] = """

**Competitive Team**
Synchro | J3 Infinityruler
Synchro | GunnerTv
\n
**Supreme Team**
Synchro | SSJ28K
Synchro | Sundey
Synchro | Angle
Synchro | FrozzTee
\n
**Elite Team**
Synchro | TSK_Fire
Synchro | H3ptic
Synchro | Unlucky Jay WTF
\n
**Ultimate Team**
No one is currently on this team. Join us in <#570734933748875265>
"""
embed["title"] = "About Us"
#embed["url"] = "https://discord.gg/3eA7HVF"
data["embeds"].append(embed)

result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
    print("Thank you, and have a great night.")
#result: https://i.imgur.com/DRqXQzA.png
